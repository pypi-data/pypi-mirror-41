import argparse
import sys
import sqlite3
import os
import json
from cravat.cravat_filter import CravatFilter
from cravat import admin_util as au
from cravat.config_loader import ConfigLoader
from cravat import util
import subprocess
import re

class CravatReport:

    def __init__ (self, cmd_args):
        self.parse_cmd_args(cmd_args)
        self.cursor = None
        self.cf = None
        self.filtertable = 'filter'
        self.colinfo = {}
        self.colnos = {}
        self.var_added_cols = []
        self.summarizing_modules = []
        self.columngroups = {}
        self.column_subs = {}
        self.connect_db()
        self.load_filter()
    
    def getjson (self, level):
        ret = None
        if self.table_exists(level) == False:
            return ret
        for row in self.cf.getiterator(level):
            row = self.substitute_val(level, row)
            return json.dumps(row) 

    def substitute_val (self, level, row):
        if level in self.column_subs:
            for i in self.column_subs[level]:
                if row[i] is not None:
                    sub = self.column_subs[level][i]
                    for target in sub:
                        row[i] = row[i].replace(target, sub[target])
        return row

    def run_level (self, level):
        if self.table_exists(level):
            if level == 'variant':
                self.cf.make_filtered_uid_table()
            elif level == 'gene':
                self.cf.make_filtered_hugo_table()
                gene_summary_datas = {}
                for mi, o, cols in self.summarizing_modules:
                    gene_summary_data = o.get_gene_summary_data(self.cf)
                    gene_summary_datas[mi.name] = [gene_summary_data, cols]
            self.write_preface(level)
            self.write_header(level)
            if level == 'variant':
                hugo_present = 'base__hugo' in self.colnos['variant']
            for row in self.cf.get_filtered_iterator(level):
                row = list(row)
                if level == 'variant':
                    if hugo_present:
                        hugo = row[self.colnos['variant']['base__hugo']]
                        generow = self.cf.get_gene_row(hugo)
                        for colname in self.var_added_cols:
                            if generow == None:
                                colval = None
                            else:
                                colval = generow[self.colnos['gene'][colname]]
                            row.append(colval)
                elif level == 'gene':
                    hugo = row[0]
                    for module_name in gene_summary_datas:
                        [gene_summary_data, cols] = gene_summary_datas[module_name]
                        if hugo in gene_summary_data:
                            row.extend([gene_summary_data[hugo][col['name']] for col in cols])
                        else:
                            row.extend([None for v in cols])
                row = self.substitute_val(level, row)
                if hasattr(self, 'keep_json_all_mapping') == False and level == 'variant':
                    colno = self.colnos['variant']['base__all_mappings']
                    all_map = json.loads(row[colno])
                    newvals = []
                    for hugo in all_map:
                        for maprow in all_map[hugo]:
                            [protid, protchange, so, transcript, rnachange] = maprow
                            if protid == None:
                                protid = '(na)'
                            if protchange == None:
                                protchange = '(na)'
                            if rnachange == None:
                                rnachange = '(na)'
                            newval = transcript + ':' + hugo + ':' + protid + ':' + so + ':' + protchange + ':' + rnachange
                            newvals.append(newval)
                    newvals.sort()
                    newcell = '; '.join(newvals)
                    row[colno] = newcell
                self.write_table_row(row)

    def run (self, tab='all'):
        self.setup()
        if tab == 'all':
            for level in self.cf.get_result_levels():
                if self.table_exists(level):
                    self.make_col_info(level)
            for level in self.cf.get_result_levels():
                if self.table_exists(level):
                    self.run_level(level)
        else:
            if tab in ['variant', 'gene']:
                for level in ['variant', 'gene']:
                    if self.table_exists(level):
                        self.make_col_info(level)
            else:
                self.make_col_info(tab)
            self.run_level(tab)
        ret = self.end()
        return ret
    
    def get_variant_colinfo (self):
        self.setup()
        level = 'variant'
        if self.table_exists(level):
            self.make_col_info(level)
        level = 'gene'
        if self.table_exists(level):
            self.make_col_info(level)
        return self.colinfo
    
    def setup (self):
        pass
    
    def end (self):
        pass
    
    def write_preface (self, level):
        pass
    
    def write_header (self, level):
        pass
    
    def write_table_row (self, row):
        pass
    
    def make_col_info (self, level):
        self.colnos[level] = {}
        # Columns from aggregator
        self.columngroups[level] = []
        sql = 'select name, displayname from ' + level + '_annotator'
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            (name, displayname) = row
            self.columngroups[level].append(
                {'name': name,
                 'displayname': displayname,
                 'count': 0})
        sql = 'select * from ' + level + '_header'
        self.cursor.execute(sql)
        columns = []
        colcount = 0
        for row in self.cursor.fetchall():
            (colname, coltitle, col_type) = row[:3]
            col_cats = json.loads(row[3]) if len(row) > 3 and row[3] else []
            col_width = row[4] if len(row) > 4 else None
            col_desc = row[5] if len(row) > 5 else None
            col_hidden = bool(row[6]) if len(row) > 6 else False
            col_ctg = row[7] if len(row) > 7 else None
            if col_ctg in ['single', 'multi'] and len(col_cats) == 0:
                sql = 'select distinct {} from {}'.format(colname, level)
                self.cursor.execute(sql)
                rs = self.cursor.fetchall()
                for r in rs:
                    col_cats.append(r[0])
            col_filterable = bool(row[8]) if len(row) > 8 else True
            column = {'col_name': colname,
                      'col_title': coltitle,
                      'col_type': col_type,
                      'col_cats': col_cats,
                      'col_width':col_width,
                      'col_desc':col_desc,
                      'col_hidden':col_hidden,
                      'col_ctg': col_ctg,
                      'col_filterable': col_filterable,
                      }
            self.colnos[level][colname] = colcount
            colcount += 1
            columns.append(column)
            groupname = colname.split('__')[0]
            for columngroup in self.columngroups[level]:
                if columngroup['name'] == groupname:
                    columngroup['count'] += 1
        if level == 'variant' and self.table_exists('gene'):
            modules_to_add = []
            q = 'select name from gene_annotator'
            self.cursor.execute(q)
            gene_annotators = [v[0] for v in self.cursor.fetchall()]
            k = 'add_gene_module_to_variant'
            if self.conf.has_key(k):
                modules_to_add = self.conf.get_val(k)
            for module in gene_annotators:
                module_info = au.get_local_module_info(module)
                if module_info == None:
                    continue
                module_conf = module_info.conf
                if 'add_to_variant_level' in module_conf:
                    if module_conf['add_to_variant_level'] == True:
                        modules_to_add.append(module)
            for module in modules_to_add:
                if not module in gene_annotators:
                    continue
                mi = au.get_local_module_info(module)
                cols = mi.conf['output_columns']
                self.columngroups[level].append({'name': mi.name, 
                                     'displayname': mi.title,
                                     'count': len(cols)})
                for col in cols:
                    self.colnos[level][colname] = colcount
                    colcount += 1
                    colname = mi.name + '__' + col['name']
                    col_type = col['type']
                    col_cats = col.get('categories',[])
                    col_width = col.get('width')
                    col_desc = col.get('desc')
                    col_hidden = col.get('hidden',False)
                    col_ctg = col.get('category', None)
                    if col_ctg in ['category', 'multicategory'] and len(col_cats) == 0:
                        sql = 'select distinct {} from {}'.format(colname, level)
                        self.cursor.execute(sql)
                        rs = self.cursor.fetchall()
                        for r in rs:
                            col_cats.append(r[0])
                    col_filterable = col.get('filterable',True)
                    column = {'col_name': colname,
                              'col_title': col['title'],
                              'col_type': col_type,
                              'col_cats': col_cats,
                              'col_width':col_width,
                              'col_desc':col_desc,
                              'col_hidden':col_hidden,
                              'col_ctg': col_ctg,
                              'col_filterable': col_filterable,
                              }
                    columns.append(column)
                    self.var_added_cols.append(colname)
        # Gene level summary columns
        if level == 'gene':
            q = 'select name from variant_annotator'
            self.cursor.execute(q)
            done_var_annotators = [v[0] for v in self.cursor.fetchall()]
            self.summarizing_modules = []
            local_modules = au.get_local_module_infos_of_type('annotator')
            for module_name in local_modules:
                mi = local_modules[module_name]
                conf = mi.conf
                if 'can_summarize_by_gene' in conf and module_name in done_var_annotators:
                    sys.path = sys.path + [os.path.dirname(mi.script_path)]
                    annot_cls = util.load_class('CravatAnnotator', mi.script_path)
                    annot = annot_cls([mi.script_path, '__dummy__'])
                    #m = __import__(module_name)
                    #o = m.CravatAnnotator(['', '__dummy__'])
                    cols = conf['gene_summary_output_columns']
                    for col in cols:
                        col['name'] = col['name'] 
                    columngroup = {}
                    columngroup['name'] = conf['name']
                    columngroup['displayname'] = conf['title']
                    columngroup['count'] = len(cols)
                    self.columngroups[level].append(columngroup)
                    for col in cols:
                        col_type = col['type']
                        col_cats = col.get('categories', [])
                        col_ctg = col.get('category', None)
                        if col_type in ['category', 'multicategory'] and len(col_cats) == 0:
                            sql = 'select distinct {} from {}'.format(colname, level)
                            self.cursor.execute(sql)
                            rs = self.cursor.fetchall()
                            for r in rs:
                                col_cats.append(r[0])
                        col_filterable = col.get('filterable', True)
                        column = {'col_name': conf['name'] + '__' + col['name'],
                                  'col_title': col['title'],
                                  'col_type': col_type,
                                  'col_cats': col_cats,
                                  'col_width':col.get('width'),
                                  'col_desc':col.get('desc'),
                                  'col_hidden':col.get('hidden',False),
                                  'col_ctg': col_ctg,
                                  'col_filterable': col_filterable,
                                  }
                        columns.append(column)
                    self.summarizing_modules.append([mi, annot, cols])
        colno = 0
        for colgroup in self.columngroups[level]:
            colno += colgroup['count']
            colgroup['lastcol'] = colno
        self.colinfo[level] = {'colgroups': self.columngroups[level], 'columns': columns}
        # report substitution
        if level in ['variant', 'gene']:
            reportsubtable = level + '_reportsub'
            if self.table_exists(reportsubtable):
                q = 'select * from {}'.format(reportsubtable)
                self.cursor.execute(q)
                rs = self.cursor.fetchall()
                self.report_substitution = {}
                for r in rs:
                    module = r[0]
                    sub = json.loads(r[1])
                    self.report_substitution[module] = sub
                self.column_subs[level] = {}
                columns = self.colinfo[level]['columns']
                for i in range(len(columns)):
                    column = columns[i]
                    [module, col] = column['col_name'].split('__')
                    if module in self.report_substitution:
                        sub = self.report_substitution[module]
                        if col in sub:
                            self.column_subs[level][i] = sub[col]
                            self.colinfo[level]['columns'][i]['reportsub'] = sub[col]

    def parse_cmd_args (self, cmd_args):
        parser = argparse.ArgumentParser()
        parser.add_argument('dbpath',
                            help='Path to aggregator output')
        parser.add_argument('-f',
            dest='filterpath',
            default=None,
            help='Path to filter file')
        parser.add_argument('-F',
            dest='filtername',
            default=None,
            help='Name of filter (stored in aggregator output)')
        parser.add_argument('--filterstring',
            dest='filterstring',
            default=None,
            help='Filter in JSON')
        parser.add_argument('-s',
            dest='savepath',
            default=None,
            help='Path to save file')
        parser.add_argument('-c',
            dest='confpath',
            help='path to a conf file')
        parser.add_argument('-t',
            dest='reporttypes',
            nargs='+',
            default=None,
            help='report types')
        parsed_args = parser.parse_args(cmd_args[1:])
        self.dbpath = parsed_args.dbpath
        self.filterpath = parsed_args.filterpath
        self.filtername = parsed_args.filtername
        self.filterstring = parsed_args.filterstring
        self.savepath = parsed_args.savepath
        self.confpath = parsed_args.confpath
        self.conf = ConfigLoader(job_conf_path=self.confpath)
        self.report_types = parsed_args.reporttypes

    def connect_db (self, dbpath=None):
        if dbpath != None:
            self.dbpath = dbpath
        if self.dbpath == None:
            sys.stderr.write('Provide a path to aggregator output')
            exit()
        if os.path.exists(self.dbpath) == False:
            sys.stderr.write(self.dbpath + ' does not exist.')
            exit()
        self.conn = sqlite3.connect(self.dbpath)
        self.cursor = self.conn.cursor()

    def load_filter (self):
        self.cf = CravatFilter(dbpath=self.dbpath)
        self.cf.loadfilter(filterpath=self.filterpath, filtername=self.filtername, filterstring=self.filterstring)

    def table_exists (self, tablename):
        sql = 'select name from sqlite_master where ' + \
            'type="table" and name="' + tablename + '"'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row == None:
            ret = False
        else:
            ret = True
        return ret

def main ():
    if len(sys.argv) < 2:
        print('Please provide a sqlite file path')
        exit()
    parser = argparse.ArgumentParser()
    parser.add_argument('dbpath',
                        help='Path to aggregator output')
    parser.add_argument('-t',
        dest='reporttypes',
        nargs='+',
        default=None,
        help='report types')
    parsed_args = parser.parse_args(sys.argv[1:])
    dbpath = parsed_args.dbpath
    report_types = parsed_args.reporttypes
    run_name = os.path.basename(dbpath).rstrip('sqlite').rstrip('.')
    output_dir = os.path.dirname(dbpath)
    avail_reporters = au.get_local_module_infos_of_type('reporter')
    avail_reporter_names = [re.sub('reporter$', '', v) for v in avail_reporters.keys()]
    cmd = ['cravat', 'dummyinput', '-n', run_name, '-d', output_dir, '--sc', '--sm', '--sa', '--sg', '--sp', '--str', '-t']
    if report_types is not None:
        cmd.extend(report_types)
    else:
        cmd.extend(avail_reporter_names)
    subprocess.run(cmd)
