function setupAllTabs () {
	for (var i = 0; i < resultLevels.length; i++) {
		var level = resultLevels[i];
		setupTab(level);
	}
}

function setupTab (tabName) {
	if (resetTab[tabName] == false) {
		return;
	}

	var tabDiv = document.getElementById("tab_" + tabName);

	var rightDivId = 'rightdiv_' + tabName;
	var rightDiv = document.getElementById(rightDivId);
	if (rightDiv == null) {
		rightDiv = getEl('div');
		rightDiv.id = rightDivId;
		rightDiv.className = 'rightdiv';
		addEl(tabDiv, rightDiv);
	}

	// Populates the right panel.
	var detailDiv = null;
	if (tabName == 'info') {
		makeInfoTab(rightDiv);
	} else if (tabName == 'variant' || tabName == 'gene') {
		makeVariantGeneTab(tabName, rightDiv);
	} else if (tabName == 'sample' || tabName == 'mapping') {
		makeSampleMappingTab(tabName, rightDiv);
	}
	addEl(tabDiv, rightDiv);

	setupEvents(tabName);

	if (tabName != 'info') {
		var stat = infomgr.getStat(tabName);
		var columns = infomgr.getColumns(tabName);
		var data = infomgr.getData(tabName);
		dataLengths[tabName] = data.length;

		makeGrid(columns, data, tabName);
		$grids[tabName].pqGrid('refresh');

		// Selects the first row.
		if (tabName == currentTab) {
			if (stat['rowsreturned'] && stat['norows'] > 0) {
				selectedRowIds[tabName] = null;
				$grids[tabName].pqGrid('setSelection', {rowIndx : 0, colIndx: 0, focus: true});
                selectedRowNos[tabName] = 0;
			}
		}
	}

	resetTab[tabName] = false;

	placeDragNSBar(tabName);
	placeCellValueDiv(tabName);

	if (loadedTableSettings != undefined && loadedTableSettings[currentTab] != undefined) {
		applyTableSetting(currentTab);
	}
	if (loadedViewerWidgetSettings != undefined && loadedViewerWidgetSettings[currentTab] != undefined) {
		applyWidgetSetting(currentTab);
	}

	changeMenu();
}

function changeTableDetailMaxButtonText () {
    var div = document.getElementById('tabledetailmaxbuttondiv');
    var button = document.getElementById('tabledetailmaxbutton');
    if (currentTab != 'variant' && currentTab != 'gene') {
        div.style.display = 'none';
        return;
    } else {
        div.style.display = 'block';
    }
    var stat = tableDetailDivSizes[currentTab]['status'];
    var text = null;
    if (stat == undefined || stat == 'both') {
        text = 'View table';
    } else if (stat == 'tablemax') {
        text = 'View detail pane';
    } else if (stat == 'detailmax') {
        text = 'View table + detail pane';
    }
    button.textContent = text;
}

function changeMenu () {
	if (currentTab == 'variant' || currentTab == 'gene' || currentTab == 'info') {
		if (currentTab == 'variant' || currentTab == 'gene') {
			turnOnMenu('layout_columns_menu');
			populateTableColumnSelectorPanel();
		}
		if (firstLoad == false) {
			turnOnMenu('layout_widgets_menu');
			populateWidgetSelectorPanel();
		}
	} else {
		turnOffMenu('layout_columns_menu');
		turnOffMenu('layout_widgets_menu');
	}
    if (shouldResizeScreen[currentTab] != false) {
        resizesTheWindow();
    }
    changeTableDetailMaxButtonText();
}

function makeInfoTab (rightDiv) {
	var tabName = 'info';
	var rightContentDiv = getEl('div');
	rightContentDiv.id = 'rightcontentdiv_' + tabName;
	rightContentDiv.className = 'rightcontentdiv';
	addEl(rightDiv, rightContentDiv);

	// Notice
	var noticeDiv = getEl('div');
	noticeDiv.className = 'infonoticediv';
	noticeDiv.id = 'infonoticediv';
	noticeDiv.textContent = ' ';
	addEl(rightContentDiv, noticeDiv);

	// Info
	var infoDiv = getEl('fieldset');
	infoDiv.id = 'info_div';
	infoDiv.style.display = 'inline-block';
	addEl(rightContentDiv, infoDiv);

	// Filter
	var filterDiv = document.getElementById('filterdiv');
	populateLoadDiv('info', filterDiv);

	// Widget Notice
	var wgNoticeDiv = getEl('fieldset');
	wgNoticeDiv.id = 'wgnoticediv';
    wgNoticeDiv.style.display = 'none';
	addEl(rightContentDiv, wgNoticeDiv);
    if (Object.keys(missingWidgets).length == 0) {
        hideWgnoticediv();
    }
	// Widgets
	var widgetDiv = getEl('div');
	widgetDiv.id = 'detailcontainerdiv_info';
	addEl(rightContentDiv, widgetDiv);
}

function toggleFilterDiv () {
	var filterDiv = document.getElementById('filterdiv');
	var filterButton = document.getElementById('filterbutton');
	var display = filterDiv.style.display;
	if (display == 'none') {
		display = 'block';
		filterButton.style.backgroundColor = 'black';
		filterButton.style.color = 'white';
	} else {
		display = 'none';
        if (filterArmed.variant != undefined && (filterArmed.variant.groups.length > 0 || filterArmed.variant.columns.length > 0)) {
            filterButton.style.backgroundColor = 'red';
        } else {
            filterButton.style.backgroundColor = 'white';
        }
		filterButton.style.color = 'black';
	}
	filterDiv.style.display = display;
}

function populateSummaryWidgetDiv () {
	var tabName = 'info';
	var outerDiv = document.getElementById('detailcontainerdiv_info');
	var widgetDivs = outerDiv.children;
	var reuseWidgets = true;
	if (widgetDivs.length == 0) {
		reuseWidgets = false;
		$(widgetDiv).packery('destroy');
		emptyElement(outerDiv);
	} else {
		widgetDivs = $(outerDiv).packery('getItemElements');
	}
	var widgetNames = Object.keys(widgetGenerators);
	if (widgetNames.length == 0) {
		/*
		var el = getEl('p');
		el.textContent = 'No summary wigdet';
		addEl(outerDiv, el);
		*/
		return;
	} else {
		var orderNums = Object.keys(detailWidgetOrder[tabName]);
		for (var i = 0; i < orderNums.length; i++) {
			var colGroupKey = detailWidgetOrder[tabName][orderNums[i]];
			if (widgetGenerators[colGroupKey] == undefined) {
				continue;
			}
			var colGroupTitle = infomgr.colgroupkeytotitle[colGroupKey];
			if (colGroupTitle == undefined) {
				colGroupTitle = widgetGenerators[colGroupKey]['name'];
			}
			if (widgetGenerators[colGroupKey][tabName] != undefined && 
				widgetGenerators[colGroupKey][tabName]['function'] != undefined) {
				var generator = widgetGenerators[colGroupKey][tabName];
				var widgetDiv = null;
				var widgetContentDiv = null;
				if (reuseWidgets) {
					widgetDiv = document.getElementById(
							'detailwidget_' + tabName + '_' + widgetName);
					widgetContentDiv = document.getElementById(
						'widgetcontentdiv_' + colGroupKey + '_' + tabName);
					if (generator['donterase'] != true) {
						$(widgetContentDiv).empty();
					}
				} else {
					[widgetDiv, widgetContentDiv] = 
						getDetailWidgetDivs(tabName, colGroupKey, colGroupTitle);
				}
				if (reuseWidgets != true) {
					widgetDiv.clientWidth = generator['width'];
					widgetDiv.clientHeight = generator['height'];
					widgetDiv.style.width = generator['width'] + 'px';
					widgetDiv.style.height = generator['height'] + 'px';
				}
                var outerDiv = document.getElementById('detailcontainerdiv_info');
				addEl(outerDiv, widgetDiv);
                try {
                    drawSummaryWidget(colGroupKey);
                } catch (err) {
                    console.log(err);
                    console.log('### continuing to the next widget ###');
                }
			}
		}
	}
	$outerDiv = $(outerDiv);
	$outerDiv.packery({
		columnWidth: widgetGridSize,
		rowHeight: widgetGridSize
	});
	var $widgets = $($outerDiv.packery('getItemElements'));
	$widgets.draggable({
		grid: [widgetGridSize, widgetGridSize],
		handle: '.detailwidgettitle',
        stop: function (evt, ui) {
            $outerDiv.packery();
        },
	}).resizable({
		grid: [widgetGridSize, widgetGridSize]
	});
	$outerDiv.packery('bindUIDraggableEvents', $widgets);
	var resizeTimeout;
	$widgets.on('resize', function (evt, ui) {
		if (resizeTimeout) {
			clearTimeout(resizeTimeout);
		}
        var sEvt = evt;
        var sUi = ui;
		resizeTimeout = setTimeout(function () {
			$(sEvt.target.parentElement).packery('fit', sUi.element[0]);
		}, 100);
	});
	if (reuseWidgets != true) {
		applyWidgetSetting('info');
	}
}

function onClickTableColumnButton () {
	if (currentTab != 'variant' && currentTab != 'gene') {
		return;
	}
	var button = evt.target;
	var panel = button.parentElement.parentElement.getElementsByClassName('tablecolumnselectorpanel')[0];
	var display = panel.style.display;
	if (display == 'none') {
		display = 'block';
		button.style.backgroundColor = '#999999';
	} else {
		display = 'none';
		button.style.backgroundColor = '#ffffff';
	}
	panel.style.display = display;
}

function onClickTableColumnSaveButton (tabName, evt) {

}

function makeVariantGeneTab (tabName, rightDiv) {
    var tableContainerDiv = null;
    var tableDiv = null;
    var northSouthDraggableDiv = null;
    var cellValueDiv = null;
    var detailDiv = null;
    var detailContainerDiv = null;

	// Table container div
    /*
    var tableContainerDivId = 'tablecontainerdiv_' + tabName;
    var tableContainerDiv = document.getElementById(tableContainerDivId);
    if (tableContainerDiv == null) {
        tableContainerDiv = getEl('div');
        tableContainerDiv.id = tableContainerDivId;
        addEl(rightDiv, tableContainerDiv);
    }
    */

	// Table div
    var tableDivId = 'tablediv_' + tabName;
	var tableDiv = document.getElementById(tableDivId);
    if (tableDiv == null) {
        tableDiv = getEl('div');
        tableDiv.id = tableDivId;
        tableDiv.className = 'tablediv';
        addEl(rightDiv, tableDiv);
    } else {
        //$(tableDiv).empty();
    }

	// Drag bar
    var northSouthDraggableDivId = 'dragNorthSouthDiv_' + tabName;
    var northSouthDraggableDiv = document.getElementById(northSouthDraggableDivId);
    if (northSouthDraggableDiv == null) {
        northSouthDraggableDiv = getEl('div');
        northSouthDraggableDiv.id = northSouthDraggableDivId;
        northSouthDraggableDiv.className = 'draggableDiv';
        $(northSouthDraggableDiv).draggable({axis:"y"});
        addEl(rightDiv, northSouthDraggableDiv);
    }

	// Cell value div
    var cellValueDivId = 'cellvaluediv_' + tabName;
    var cellValueDiv = document.getElementById(cellValueDivId);
    if (cellValueDiv == null) {
        cellValueDiv = getEl('div');
        cellValueDiv.id = cellValueDivId;
        cellValueDiv.className = 'cellvaluediv';
        var input = getEl('input');
        input.id = 'cellvaluetext_' + tabName;
        input.type = 'text';
        input.style.width = '100%';
        addEl(cellValueDiv, input);
        addEl(rightDiv, cellValueDiv);
    }

	// Detail div
    var detailDivId = 'detaildiv_' + tabName;
    var detailDiv = document.getElementById(detailDivId);
    if (detailDiv == null) {
        detailDiv = getEl('div');
        detailDiv.id = detailDivId;
        detailDiv.className = 'detaildiv';
        var detailContainerWrapDiv = getEl('div');
        detailContainerWrapDiv.className = 'detailcontainerwrapdiv';
        var heightSetting = loadedHeightSettings['detail_' + tabName];
        if (heightSetting != undefined) {
            detailDiv.style.height = heightSetting;
        }
        addEl(detailDiv, detailContainerWrapDiv);
    }

	// Detail content div
    var detailContainerDivId = 'detailcontainerdiv_' + tabName;
    var detailContainerDiv = document.getElementById(detailContainerDivId);
    if (detailContainerDiv == null) {
        detailContainerDiv = getEl('div');
        detailContainerDiv.id = detailContainerDivId;
        detailContainerDiv.className = 'detailcontainerdiv';
        addEl(detailContainerWrapDiv, detailContainerDiv);
        addEl(rightDiv, detailDiv);
    }
}

function onClickDetailRedraw () {
	var tabName = currentTab;
	var div = document.getElementById('detailcontainerdiv_' + tabName);
	$(div).packery();
}

function onClickDetailReset () {
	var tabName = currentTab;
	var div = document.getElementById('detailcontainerdiv_' + tabName);
	var widgets = div.children;
	for (var i = 0; i < widgets.length; i++) {
		var widget = widgets[i];
		var widgetName = widget.getAttribute('widgetkey');
		var generator = widgetGenerators[widgetName][currentTab];
		widget.style.top = '0px';
		widget.style.left = '0px';
		widget.style.width = generator['width'] + 'px';
		widget.style.height = generator['height'] + 'px';
	}
	$(div).packery();
}

function makeSampleMappingTab (tabName, rightDiv) {
	var tableDiv = getEl('div');
	tableDiv.id = 'tablediv_' + tabName;
	tableDiv.className = 'tablediv';
	addEl(rightDiv, tableDiv);
}

function populateWgNoticeDiv (noWgAnnotModules) {
	var wgNoticeDiv = document.getElementById('wgnoticediv');
	if (Object.keys(noWgAnnotModules).length == 0) {
		wgNoticeDiv.style.display = 'none';
		return;
	} else {
        wgNoticeDiv.style.display = 'block';
    }
    emptyElement(wgNoticeDiv);
	var legend = getEl('legend');
	legend.className = 'section_header';
	addEl(legend, getTn('Missing Widgets'));
	addEl(wgNoticeDiv, legend);
	wgNoticeDiv.className = 'detailContent';
	var msg = 'Your system does not have viwer widgets for the following annotator results are not installed in the system. ';
	msg += 'If you want to install viewer widgets for them, click the buttons for the annotators.';
	var span = getEl('span');
	addEl(wgNoticeDiv, addEl(span, getTn(msg)));
	addEl(wgNoticeDiv, getEl('br'));
	addEl(wgNoticeDiv, getEl('br'));
	var div = getEl('div');
	var moduleKeys = Object.keys(noWgAnnotModules);
	for (var i = 0; i < moduleKeys.length; i++) {
		var moduleKey = moduleKeys[i];
		var moduleTitle = noWgAnnotModules[moduleKey];
		var button = getEl('button');
        button.setAttribute('module', moduleKey);
		button.style.marginRight = '20px';
		button.style.marginBottom = '10px';
		button.textContent = moduleTitle;
        button.addEventListener('click', function (evt) {
            installWidgetsForModule(evt.target.getAttribute('module'));
        });
		addEl(div, button);
	}
	addEl(wgNoticeDiv, div);
}

function installWidgetsForModule (moduleKey) {
    $.get('/store/installwidgetsformodule', {'name': moduleKey}).done(function () {
        checkWidgets();
    });
}

function populateInfoDiv (infoDiv) {
	// Title
	var span = getEl('legend');
	span.className = 'section_header';
	addEl(span, getTn('Result Information'));
	addEl(infoDiv, span);

	var keys = Object.keys(infomgr.jobinfo);
	var table = getEl('table');
	var tbody = getEl('tbody');
	for (var i = 0; i < keys.length; i++) {
		var key = keys[i];
		var val = infomgr.jobinfo[key];
		var tr = getEl('tr');
		var td = getEl('td');
		td.style.minWidth = '200px';
		var span = getEl('span');
		span.className = 'detailHeader';
		addEl(tr, addEl(td, addEl(span, getTn(key))));
		var td = getEl('td');
		var span = getEl('span');
        if (key == 'Number of unique input variants') {
            span.id = 'numberofuniqueinputvariants_span';
        }
		span.className = 'detailContent';
		addEl(tr, addEl(td, addEl(span, getTn(val))));
		addEl(tbody, tr);
	}
	addEl(table, tbody);
	addEl(infoDiv, table);
}

function populateWidgetSelectorPanel () {
	var tabName = currentTab;
	var panelDiv = document.getElementById('widgets_showhide_select_div');
	panelDiv.innerHTML = '';
	panelDiv.style.width = '300px';
	panelDiv.style.maxHeight = '400px';
	panelDiv.style.overflow = 'auto';

	var button = getEl('button');
	button.style.backgroundColor = 'white';
	button.textContent = 'Redraw';
	button.addEventListener('click', function (evt, ui) {
		onClickDetailRedraw();
	});
	addEl(panelDiv, button);

	var button = getEl('button');
	button.style.backgroundColor = 'white';
	button.textContent = 'Reset';
	button.addEventListener('click', function (evt, ui) {
		onClickDetailReset();
	});
	addEl(panelDiv, button);

	var button = getEl('button');
	button.style.backgroundColor = 'white';
	button.textContent = 'Hide all';
	button.addEventListener('click', function (evt, ui) {
		changeWidgetShowHideAll(false);
	});
	addEl(panelDiv, button);

	var button = getEl('button');
	button.style.backgroundColor = 'white';
	button.textContent = 'Show all';
	button.addEventListener('click', function (evt, ui) {
		changeWidgetShowHideAll(true);
	});
	addEl(panelDiv, button);

	var widgetNames = Object.keys(widgetGenerators);
	for (var i = 0; i < widgetNames.length; i++) {
		var widgetName = widgetNames[i];
		if (widgetGenerators[widgetName][tabName] != undefined &&
			widgetGenerators[widgetName][tabName]['function'] != undefined &&
			usedAnnotators[tabName].includes(infomgr.widgetReq[widgetName])) {
			var div = getEl('div');
			div.style.padding = '4px';
			var input = getEl('input');
			input.id = 'widgettogglecheckbox_' + tabName + '_' + widgetName;
			input.type = 'checkbox';
            var vwsT = viewerWidgetSettings[tabName];
            if (vwsT == undefined) {
                vwsT = [];
                viewerWidgetSettings[tabName] = vwsT;
            }
            var vws = getViewerWidgetSettingByWidgetkey(tabName, widgetName);
            if (vws == null) {
                input.checked = true;
            } else {
                var display = vws['display'];
                if (display != 'none') {
                    input.checked = true;
                } else {
                    input.checked = false;
                }
            }
			input.setAttribute('widgetname', widgetName);
			input.addEventListener('click', function (evt) {
				onClickWidgetSelectorCheckbox(tabName, evt);
			});
			addEl(div, input);
			var span = getEl('span');
			addEl(span, getTn(infomgr.colgroupkeytotitle[widgetName]));
			addEl(div, span);
			addEl(panelDiv, div);
		}
	}
}

function onClickWidgetPinButton (evt, tabName) {
	var widget = evt.target.parentElement.parentElement.parentElement;
	var container = widget.parentElement;
	var button = evt.target;
	var pinned = button.classList.contains('pinned');
	if (pinned) {
		button.classList.remove('pinned');
		button.classList.add('unpinned');
		button.src = '/result/images/pin.png';
		$(container).packery('unstamp', widget);
	} else {
		button.src = '/result/images/pin-2.png';
		button.classList.remove('unpinned');
		button.classList.add('pinned');
		$(container).packery('stamp', widget);
	}
}

function onClickWidgetCloseButton (tabName, evt) {
	var widgetName = evt.target.getAttribute('widgetname');
	showHideWidget(tabName, widgetName, false);
	var button = document.getElementById(
			'widgettogglecheckbox_' + tabName + '_' + widgetName);
	button.checked = false;
}

function changeWidgetShowHideAll (checked) {
	var tabName = currentTab;
	var div = document.getElementById('detailcontainerdiv_' + tabName);
    var widgets = $(div).packery('getItemElements');
    for (var i = 0; i < widgets.length; i++) {
        var widget = widgets[i];
        var widgetName = widget.getAttribute('widgetkey');
        document.getElementById('widgettogglecheckbox_' + tabName + '_' + widgetName).checked = checked;
        showHideWidget(tabName, widgetName, checked)
    }
}

function onClickWidgetSelectorCheckbox (tabName, evt) {
	var button = evt.target;
	var checked = button.checked;
	var widgetName = button.getAttribute('widgetname');
	showHideWidget(tabName, widgetName, checked)
}

function showHideWidget (tabName, widgetName, state) {
	var widget = document.getElementById(
			'detailwidget_' + tabName + '_' + widgetName);
	if (state == false) {
		widget.style.display = 'none';
	} else {
		widget.style.display = 'block';
        if (currentTab == 'info') {
            var dcd = widget.getElementsByClassName('detailcontentdiv')[0];
            if (dcd.innerHTML == '') {
                    drawSummaryWidget(widgetName);
            }
        }
	}
	var $detailContainerDiv = $(document.getElementById('detailcontainerdiv_' + tabName));
	$detailContainerDiv.packery('fit', widget);
}

function drawSummaryWidget (widgetName) {
	var widgetContentDiv = document.getElementById('widgetcontentdiv_' + widgetName + '_info');
	emptyElement(widgetContentDiv);
	var generator = widgetGenerators[widgetName]['info'];
    /*
    if (generator['hidden'] == true) {
        for (var i = 0; i < viewerWidgetSettings['info'].length; i++) {
            var vws = viewerWidgetSettings['info'][i];
            if (vws.id == 'detailwidget_info_' + widgetName) {
                vws.display = 'none';
                break;
            }
        }
        return;
    }
    */
	var callServer = generator['callserver'];
	if (callServer) {
		$.get('/result/runwidget/' + widgetName, {dbpath: dbPath}).done(function (response) {
			var data = response['data'];
			if (data == {}) {
			} else {
                try {
                    generator['function'](widgetContentDiv, data);
                } catch (e) {
                    console.log(e);
                }
			}
		});
	} else {
        try {
            generator['function'](widgetContentDiv);
        } catch (e) {
            console.log(e);
        }
	}
}

function setupEvents (tabName) {
    $("#dragNorthSouthDiv_" + tabName).on('dragstop', function(){
	    afterDragNSBar(this, tabName);
    });

    $('.ui-icon-circle-triangle-n').on('click', function(){
	    minimizeOrMaxmimizeTheDetailsDiv(this, 'minimize');
    });

    /*
   $(document).keydown(function(button){
	   switch(button.which){
	   case 27:
		   if (tabName == currentTab){
			   if (document.getElementById("splashMupitBckRound_" + tabName) != null){
				   eraseMuPITPopUp(currentTab);
			   }
		   }
	   }
   });
   */
}

function placeDragNSBar (tabName) {
	var dragBar = document.getElementById('dragNorthSouthDiv_' + tabName);
	if (! dragBar) {
		return;
	}
	var tableDiv = document.getElementById('tablediv_' + tabName);
	var tableDivHeight = tableDiv.offsetHeight;
	dragBar.style.top = tableDivHeight + 29;
}

function placeCellValueDiv (tabName) {
	var div = document.getElementById('cellvaluediv_' + tabName);
	if (! div) {
		return;
	}
	var tableDiv = document.getElementById('tablediv_' + tabName);
	var tableDivHeight = tableDiv.offsetHeight;
	div.style.top = tableDivHeight + ARBITRARY_HEIGHT_SUBTRACTION - 10;
}

function addLeftPanelFieldSet (tabName, parent, fieldSetName) {
	var fieldSet = getEl('fieldset');
	var fieldSetId = fieldSetName.toLowerCase().replace(/ /g, '_');
	fieldSet.id = fieldSetId + '_fieldset_' + tabName;
	fieldSet.style.display = 'block';
	var legend = getEl('legend');
	legend.className = 'toggle_header_' + tabName;
	legend.style.cursor = 'pointer';
	legend.style.fontSize = '14px';
	legend.style.fontWeight = 'bold';
	addEl(legend, getTn(fieldSetName));
	var img = getEl('img');
	img.src = '/result/images/minus.png';
	img.style.width = '11px';
	img.style.height = '11px';
	addEl(legend, img);
	addEl(fieldSet, legend);
	var innerDiv = getEl('div');
	innerDiv.id = fieldSetId + '_innerdiv_' + tabName;
	innerDiv.className = 'collapsible';
	addEl(fieldSet, innerDiv);
	addEl(parent, fieldSet);
}

function makeGrid (columns, data, tabName) {
	dataLengths[tabName] = data.length;

	var $tableDiv = $('#tablediv_' + tabName);

	var gridObj = loadGridObject(columns, data, tabName, jobId, 'main');
	if (gridObj == undefined) {
		return;
	}

	gridObj.filterModel = {on: true, header: true, type: 'local'};

	gridObj.headerCellClick = function (evt, ui) {
		var $grid = $grids[tabName];
		var sortModel = $grid.pqGrid('option', 'sortModel');
		if (evt.shiftKey) {
			sortModel.single = false;
		} else {
			sortModel.single = true;
		}
		$grid.pqGrid('option', 'sortModel', sortModel);
	};

	// Creates the grid.
    try {
        $tableDiv.pqGrid('destroy');
    } catch (e) {
    }
	var $grid = $tableDiv.pqGrid(gridObj);
	$grids[tabName] = $grid;
	gridObjs[tabName] = gridObj;

	// Adds the footer.
	var footer = $grid.find('.pq-grid-footer')[0];
	var span = getEl('span');
	span.id = 'footertext_' + tabName;
	var button = getEl('button');
	button.id = 'exportbutton_' + tabName;
	button.onclick = function(event) {
		var a = getEl('a');
		var tsvContent = getExportContent(tabName);
		a.href = window.URL.createObjectURL(
				new Blob([tsvContent], {type: 'text/tsv'}));
		a.download = jobId + '_' + tabName + '.tsv';
		document.body.appendChild(a);
		a.click();
		document.body.removeChild(a);
	};
	addEl(button, getTn('Export'));
	addEl(footer, span);
	addEl(footer, button);
	var lenStr = dataLengths[tabName] + ' total rows';
	document.getElementById('footertext_' + tabName).textContent = lenStr;
}

function emptyElement (elem) {
    if (elem == null) {
        return;
    }
	var last = null;
    while (last = elem.lastChild) {
    	elem.removeChild(last);
    }
}

function getFilterCol (columnKey) {
	for (var i = 0; i < filterCols.length; i++) {
		var colModel = filterCols[i].colModel;
		for (var j = 0; j < colModel.length; j++) {
			var column = colModel[j];
			if (column.col == columnKey) {
				return column;
			}
		}
	}
	return null;
}

function getLoadSelectorDiv (tabName) {
	var div = getEl('div');

	// Selector
	var selector = getEl('select');
	selector.id = 'filterselect';
	selector.className = 'inlineselect';
	var option = new Option('Choose a column to filter', 'none');
	selector.options.add(option);
	for (var i = 0; i < filterCols.length; i++) {
		var filterCol = filterCols[i];
		var columnGroupName = filterCol.title;
		var colModel = filterCol.colModel;
		for (var j = 0; j < colModel.length; j++) {
			var column = colModel[j];
			if (column.retfilt == true) {
				option = new Option(column.colgroup + ' | ' + column.title, column.col);
				selector.options.add(option);
			}
		}
	}

	selector.onchange = function (evt) {
		onChangeFilterSelector(null, null, null, null);
	}
	addEl(div, selector);

	// Select detail div
	var selectDetailDiv = getEl('div');
	selectDetailDiv.id = 'selectdetaildiv';
	selectDetailDiv.style.display = 'inline-block';
	addEl(div, selectDetailDiv);

	return div;
}

function updateLoadMsgDiv (msg) {
	var msgDiv = document.getElementById('load_innerdiv_msg_info');
	emptyElement(msgDiv);
	addEl(msgDiv, getTn(msg));
}

function setFilterSelect (div) {
	var selectDiv = div.parentElement.previousSibling;
	var col = div.getAttribute('col');
	var retfilttype = div.getAttribute('retfilttype');
	var val1 = div.getAttribute('val1');
	var val2 = div.getAttribute('val2');
	var checked = div.getAttribute('checked');
	var select = selectDiv.getElementsByClassName('inlineselect')[0];
	onChangeFilterSelector(col, retfilttype, val1, val2, checked);
}

function populateLoadDiv (tabName, filterDiv) {
	// Title
	var legend = getEl('legend');
	legend.className = 'section_header';
	addEl(legend, getTn('Variant Filters'));

	// Save Filter Set button
	var button = getEl('button');
	button.style.marginLeft = '10px';
	button.onclick = function(event) {
		saveFilterSettingAs();
	};
	addEl(button, getTn('Save...'));
	addEl(legend, button);

	// Load Filter Set button
	var button = getEl('button');
	button.style.marginLeft = '10px';
	button.onclick = function(event) {
		var filterDiv = document.getElementById('load_filter_select_div');
	 	var display = filterDiv.style.display;
	 	if (display == 'none') {
	 		filterDiv.style.display = 'block';
	 		loadFilterSettingAs();
	 	} else {
	 		filterDiv.style.display = 'none';
	 	}
	};
	addEl(button, getTn('Load...'));
	addEl(legend, button);

    // Delete Filter Set button
    var button = getEl('button');
    button.style.marginLeft = '10px';
    button.onclick = function (evt) {
        deleteFilterSettingAs();
    }
    addEl(button, getTn('Delete...'));
    addEl(legend, button);

	// Filter name div
	var div = getEl('div');
	div.id = 'load_filter_select_div';
	div.style.display = 'none';
	div.style.position = 'absolute';
	div.style.left = '198px';
	div.style.padding = '6px';
	div.style.overflow = 'auto';
	div.style.backgroundColor = 'rgb(232, 232, 232)';
	div.style.border = '1px solid black';
	addEl(legend, div);

	addEl(filterDiv, legend);

	// Description
	var div = getEl('div');
	var p = getEl('p');
	p.textContent = 'Add variant filters below. Click "Count" to count the '
				   +'number of variants passing the filter. Click "Update" to '
				   +'apply the filter.'
	addEl(div, p);
	addEl(filterDiv, div);

    // Filter
    var div = getEl('div');
    div.id = 'filterwrapdiv';
    populateFilterWrapDiv(div);
    $(filterDiv).append(div);

    // Message
    var div = getEl('div');
    div.id = prefixLoadDiv + 'msg_' + tabName;
    div.style.height = '20px';
    div.style.fontFamily = 'Verdana';
    div.style.fontSize = '12px';
    addEl(filterDiv, div);

    // Count button
    var button = getEl('button');
    button.id = 'count_button';
    button.onclick = function (evt) {
        makeFilterJson();
        infomgr.count(dbPath, 'variant', updateLoadMsgDiv);
    }
    button.textContent = 'Count';
    addEl(filterDiv, button);

    // Update button
    var button = getEl('button');
    button.id = 'load_button';
    button.onclick = function(evt) {
        toggleFilterDiv();
        evt.target.disabled = true;
        var infoReset = resetTab['info'];
        resetTab = {'info': infoReset};
        showSpinner(tabName, this);
        makeFilterJson();
        loadData(false, null);
    };
    addEl(button, getTn('Update'));
    addEl(filterDiv, button);

    // Close button
    var button = getEl('div');
    button.style.position = 'absolute';
    button.style.top = '2px';
    button.style.right = '4px';
    button.style.fontSize = '20px';
    button.textContent = 'X';
    button.style.cursor = 'default';
    button.addEventListener('click', function (evt) {
        toggleFilterDiv();
    });
    addEl(filterDiv, button);
}

function onClickFilterLevelButton (button) {
    var simpleFilterDiv = document.getElementById('filter-root-group-div-simple');
    var advancedFilterDiv = document.getElementById('filter-root-group-div-advanced');
    if (button.classList.contains('filter-level-simple')) {
        button.classList.remove('filter-level-simple');
        button.classList.add('filter-level-advanced');
        simpleFilterDiv.style.display = 'none';
        advancedFilterDiv.style.display = null;
    } else if (button.classList.contains('filter-level-advanced')) {
        button.classList.remove('filter-level-advanced');
        button.classList.add('filter-level-simple');
        simpleFilterDiv.style.display = null;
        advancedFilterDiv.style.display = 'none';
    }
}

function populateFilterWrapDiv (div) {
    var button = getEl('span');
    button.className = 'filter-level-button';
    button.addEventListener('click', function (evt) {
		onClickFilterLevelButton(evt.target);
    });
	button.classList.add('filter-level-simple');
    addEl(div, button);
	addEl(div, getEl('br'));
	var filter = undefined;
	var filterSimple = undefined;
	var advancedColumnsPresent = false;
	if (filterJson.hasOwnProperty('variant')) {
		filter = filterJson;
		// Make copy without groups for simple filter
		filterSimple = JSON.parse(JSON.stringify(filter));
		filterSimple.variant.groups = [];
		// Also exclude columns that are only available in advanced
		const topFilterCols = filterSimple.variant.columns;
		const topSimpleCols = []
		for (let i=0; i<topFilterCols.length; i++) {
			let filterCol = topFilterCols[i];
			let colModel = getFilterColByName(filterCol.column);
			if (colModel.filterable) {
				topSimpleCols.push(filterCol)
			} else {
				advancedColumnsPresent = true;
			}
		}
		filterSimple.variant.columns = topSimpleCols;
	}
	var filterRootGroupDivSimple = makeFilterRootGroupDiv(filterSimple, 'filter-root-group-div-simple', 'simple');
	$(div).append(filterRootGroupDivSimple);
	button.classList.remove('filter-level-simple'); // Must toggle to advanced so that advanced filter uses all columns in rules selector
	button.classList.add('filter-level-advanced');
	var filterRootGroupDivAdvanced = makeFilterRootGroupDiv(filter, 'filter-root-group-div-advanced', 'advanced');
	button.classList.remove('filter-level-advanced'); // Toggle back
	button.classList.add('filter-level-simple');
	$(div).append(filterRootGroupDivAdvanced);
	filterRootGroupDivSimple[0].style.display = null;
	filterRootGroupDivAdvanced[0].style.display = 'none';
	if ((filter && filter.variant.groups.length > 0) || advancedColumnsPresent) { // Advanced filter
		filterRootGroupDivSimple[0].style.display = 'none';
		filterRootGroupDivAdvanced[0].style.display = null; // Setting element.style null means inherited css style is used
		button.classList.remove('filter-level-simple');
		button.classList.add('filter-level-advanced');
	}
}

function populateTableColumnSelectorPanel () {
	var tabName = currentTab;
	var wholeDiv = document.getElementById('columns_showhide_select_div');
	wholeDiv.innerHTML = '';
	wholeDiv.style.width = '400px';
	wholeDiv.style.height = '400px';
	wholeDiv.style.overflow = 'auto';
	var columnGroupsForTab = infomgr.getColumnGroups(tabName);
	var columnGroupNames = Object.keys(columnGroupsForTab);
	var columns = infomgr.getColumns(tabName);
	for (var i = 0; i < columnGroupNames.length; i++) {
		var colGroupNo = i;
		var columnGroupName = columnGroupNames[i];
		var columnGroupColumnKeys = columnGroupsForTab[columnGroupName];

		// Group div
		var groupDiv = document.createElement('fieldset');
		groupDiv.id = columnGroupPrefix + '_' + tabName + '_' + columnGroupName + '_id';
		groupDiv.className = columnGroupPrefix + '_' + tabName + '_class';
		var legend = getEl('legend');
		legend.style.fontSize = '14px';
		legend.style.fontWeight = 'bold';
		var checkbox = getEl('input');
		checkbox.type = 'checkbox';
		checkbox.checked = true;
		checkbox.setAttribute('colgroupno', i);
		checkbox.setAttribute('colgroupname', columnGroupName);
		checkbox.addEventListener('change', function (evt, ui) {
			var colGroupName = evt.target.getAttribute('colgroupname');
			var cols = infomgr.getColumnGroups(currentTab)[colGroupName];
			var checkboxes = this.parentElement.parentElement.getElementsByClassName('colcheckbox');
			var checked = this.checked;
			for (var i = 0; i < checkboxes.length; i++) {
				var checkbox = checkboxes[i];
				checkbox.checked = checked;
			}
			updateTableColumns(tabName);
		});
		addEl(legend, checkbox);
		addEl(legend, getTn(columnGroupName));
		addEl(groupDiv, legend);

		// Columns
		var columnsDiv = document.createElement('div');
		for (var columnKeyNo = 0; columnKeyNo < columnGroupColumnKeys.length; 
				columnKeyNo++) {
			var columnKey = columnGroupColumnKeys[columnKeyNo];
			var column = columns[infomgr.getColumnNo(tabName, columnKey)];
			var span = getEl('span');
			span.textContent = '\xA0';
			addEl(columnsDiv, span);
			var checkbox = getEl('input');
			checkbox.id = columnGroupPrefix + '_' + tabName + '_' + columnGroupName + '_' + column.col + '_' + '_checkbox';
			checkbox.className = 'colcheckbox';
			checkbox.type = 'checkbox';
			checkbox.checked = !column.hidden;
			checkbox.setAttribute('colgroupname', columnGroupName);
			checkbox.setAttribute('col', column.col);
			checkbox.setAttribute('colno', columnKeyNo);
			checkbox.addEventListener('change', function (evt, ui) {
				updateTableColumns(tabName);
			});
			addEl(columnsDiv, checkbox);
			var span = document.createElement('span');
			span.textContent = column.title;
			addEl(columnsDiv, span);
			var br = getEl('br');
			addEl(columnsDiv, br);
		}
		addEl(groupDiv, columnsDiv);
		addEl(wholeDiv, groupDiv);
	}
}

function updateTableColumns (tabName) {
	var selectorPanel = document.getElementById('columns_showhide_select_div');
	var checkboxes = selectorPanel.getElementsByClassName('colcheckbox');
	var colModel = $grids[tabName].pqGrid('option', 'colModel');
	for (var i = 0; i < checkboxes.length; i++) {
		var checkbox = checkboxes[i];
		var colgroupname = checkbox.getAttribute('colgroupname');
		var colkey = checkbox.getAttribute('col');
		var colno = checkbox.getAttribute('colno');
		var checked =  ! checkbox.checked;
		for (var j = 0; j < colModel.length; j++) {
			var cols = colModel[j].colModel;
			for (var k = 0; k < cols.length; k++) {
				var col = cols[k];
				if (col.colgroup == colgroupname && col.col == colkey) {
					cols[k].hidden = checked;
					break;
				}
			}
		}
	}
	$grids[tabName].pqGrid('option', 'colModel', colModel).pqGrid('refresh');
}
function showSpinner (tabName, elem) {
	spinner = getEl('img');
	spinner.src = '/result/images/spinner.gif';
	spinner.style.width = '15px';
	addEl(elem.parentElement, spinner);
}

function pickThroughAndChangeCursorClasses(domElement, classToSkip, 
			classToAdd) {
	   var classNames = domElement.className;
	   var arrayClasses = classNames.split(" ");
	   var newArrayClassNames = [];
	   for(var i=0; i<arrayClasses.length; i++){
		   if (arrayClasses[i] != classToSkip){
			   newArrayClassNames.push(arrayClasses[i]);
		   }
	   }
	   newArrayClassNames.push(classToAdd);
	   domElement.className = newArrayClassNames.join(" ");	
}

function loadGridObject(columns, data, tabName, tableTitle, tableType) {
	var rightDiv = null;
	var detailDiv = document.getElementById('detaildiv_' + tabName);
	var dragBar = document.getElementById('dragNorthSouthDiv_' + tabName);
	var rightDiv = document.getElementById('rightdiv_' + tabName);

	if (rightDiv == null) {
		return;
	}

	var rightDivWidth = rightDiv.offsetWidth;
	var rightDivHeight = rightDiv.offsetHeight;
	var dragBarHeight = 0;
	if (dragBar) {
		dragBarHeight = dragBar.offsetHeight;
	}
	var detailDivHeight = 0;
	if (detailDiv) {
        if (loadedHeightSettings['detail_' + tabName] == undefined) {
            if (rightDivHeight < 660) {
                detailDivHeight = 250;
            } else {
                detailDivHeight = detailDiv.offsetHeight;
            }
        } else {
            detailDivHeight = Number(loadedHeightSettings['detail_' + tabName].replace('px', ''));
        }
        detailDiv.style.height = detailDivHeight + 'px';
	}

	var gridObject = new Object();
	gridObject.title = tableTitle;
	gridObject.width = rightDivWidth;
	gridObject.height = rightDivHeight - dragBarHeight - detailDivHeight - ARBITRARY_HEIGHT_SUBTRACTION - 15;
	gridObject.virtualX = false;
	gridObject.virtualY = true;
	gridObject.wrap = false;
	gridObject.hwrap = true;
	gridObject.sortable = true;
	gridObject.numberCell = {show: false};
	gridObject.showTitle = false;
	gridObject.selectionModel = {type: 'cell', mode: 'block'};
	gridObject.hoverMode = 'cell';
	gridObject.colModel = infomgr.getColModel(tabName);
	gridObject.dataModel = {data: data};
	var sortColumnToUse = 'input_line_number';
	gridObject.sortModel = {
			cancel: true, 
			on: true, 
			type: 'local', 
			single: true, 
			number: true, 
			sorter: [{dataIndx: infomgr.getColumnNo(tabName, 
						sortColumnToUse), dir: 'up'}]};
	gridObject.selectChange = function (event, ui) {
		var clickInfo = ui.selection['_areas'][0];
		var rowNo = clickInfo['r1'];
		var colNo = clickInfo['c1'];
		var rowData = $grids[tabName].pqGrid('getData')[rowNo];
		var cellData = rowData[colNo];
		var valueText = null;
		if (cellData == undefined || cellData == '' || cellData == null) {
			valueText = '';
		} else {
			valueText = cellData;
		}
		var celltextel = document.getElementById('cellvaluetext_' + tabName);
		if (celltextel) {
			celltextel.value = valueText;
		}
        if (selectedRowNos[tabName] != undefined) {
            var row = $grids[tabName].pqGrid('getRow', {rowIndxPage: selectedRowNos[tabName]});
            row.css('background-color', 'white');
        }
        var row = $grids[tabName].pqGrid('getRow', {rowIndxPage: rowNo});
        row.css('background-color', '#ffc500');
		if (rowData != undefined) {
			if (selectedRowIds[tabName] == null || selectedRowIds[tabName] != rowData[0]) {
				selectedRowIds[tabName] = rowData[0];
				selectedRowNos[tabName] = rowNo;
				showVariantDetail(rowData, tabName);
			}
		}
	};
	gridObject.beforeSort = function (evt, ui) {
		if (evt.shiftKey) {
			ascendingSort = {};
			for (var i = 0; i < ui.sorter.length; i++) {
				var sorter = ui.sorter[i];
				ascendingSort[sorter.dataIndx] = (sorter.dir == 'up');
			}
		} else {
			ui.sorter = [ui.sorter[ui.sorter.length - 1]];
			gridObject.sortModel.sorter = ui.sorter;
			if (ui.sorter[0] != undefined) {
				var sorter = ui.sorter[0];
				ascendingSort = {};
				ascendingSort[sorter.dataIndx] = (sorter.dir == 'up');
			}
		}
	};
	gridObject.sortDir = 'up';
	gridObject.options = {
			showBottom: true, 
			dragColumns: {enabled: false}
	};
	gridObject.filter = function () {
		this.scrollRow({rowIndxPage: 0});
	};
	gridObject.collapsible = {on: false, toggle: false};
	gridObject.roundCorners = false;
	gridObject.stripeRows = true;
	gridObject.cellDblClick = function (evt, ui) {
	}
	gridObject.columnOrder = function (evt, ui) {
	}
    gridObject.refresh = function (evt, ui) {
        var selRowNo = selectedRowNos[tabName];
        if (selRowNo >= ui.initV && selRowNo <= ui.finalV) {
            var row = $grids[tabName].pqGrid('getRow', {rowIndxPage: selRowNo});
            row.css('background-color', '#ffc500');
        }
	}
	gridObject.refreshHeader = function () {
		for (let i=0; i<this.colModel.length; i++) {
			col = this.colModel[i];
			if (col.desc !== null) {
				$(this.getCellHeader({colIndx:col.dataIndx})).attr('title',col.desc).tooltip();
			}
		}
	}
	return gridObject;
}

function minimizeOrMaxmimizeDetailDiv () {
    var tabName = currentTab;
    var tableDiv = document.getElementById('tablediv_' + tabName);
    var detailDiv = document.getElementById('detaildiv_' + tabName);
    var rightDiv = document.getElementById('rightdiv_' + tabName);
    if (tableDetailDivSizes[tabName] == undefined) {
        tableDetailDivSizes[tabName] = {'status': null};
    }
    if (tableDetailDivSizes[tabName]['status'] == null) {
        tableDetailDivSizes[tabName] = {'tablediv': {'width': tableDiv.offsetWidth, 'height': tableDiv.offsetHeight}, 'detaildiv': {'width': detailDiv.offsetWidth, 'height': detailDiv.offsetHeight}, 'status': 'detailmax'};
        tableDiv.style.display = 'none';
        detailDiv.style.height = (rightDiv.offsetHeight - 10) + 'px';
        document.getElementById('dragNorthSouthDiv_' + tabName).style.display = 'none';
        document.getElementById('cellvaluediv_' + tabName).style.display = 'none';
    } else {
        if (tableDetailDivSizes[tabName]['status'] == 'tablemax') {
            minimizeOrMaxmimizeTableDiv();
        }
        tableDiv.style.display = 'block';
        detailDiv.style.height = tableDetailDivSizes[tabName]['detaildiv']['height'];
        document.getElementById('dragNorthSouthDiv_' + tabName).style.display = 'block';
        document.getElementById('cellvaluediv_' + tabName).style.display = 'block';
        tableDetailDivSizes[tabName] = {'status': null};
    }
}

function minimizeOrMaxmimizeTableDiv () {
    var tabName = currentTab;
    var tableDiv = document.getElementById('tablediv_' + tabName);
    var detailDiv = document.getElementById('detaildiv_' + tabName);
    var rightDiv = document.getElementById('rightdiv_' + tabName);
    if (tableDetailDivSizes[tabName] == undefined) {
        tableDetailDivSizes[tabName] = {'status': null};
    }
    if (tableDetailDivSizes[tabName]['status'] == null) {
        if (tableDetailDivSizes[tabName]['status'] == 'detailmax') {
            minimizeOrMaxmimizeDetailDiv();
        }
        tableDetailDivSizes[tabName] = {'tablediv': {'width': tableDiv.offsetWidth, 'height': tableDiv.offsetHeight}, 'detaildiv': {'width': detailDiv.offsetWidth, 'height': detailDiv.offsetHeight}, 'status': 'tablemax'};
        var tableHeight = rightDiv.offsetHeight;
        tableDiv.style.height = tableHeight + 'px';
        $grids[tabName].pqGrid('option', 'height', tableHeight).pqGrid('refresh');
        detailDiv.style.display = 'none';
        document.getElementById('dragNorthSouthDiv_' + tabName).style.display = 'none';
        document.getElementById('cellvaluediv_' + tabName).style.display = 'none';
    } else {
        detailDiv.style.display = 'block';
        var tableHeight = tableDetailDivSizes[tabName]['tablediv']['height'];
        tableDiv.style.height = tableHeight + 'px';
        $grids[tabName].pqGrid('option', 'height', tableHeight).pqGrid('refresh');
        document.getElementById('dragNorthSouthDiv_' + tabName).style.display = 'block';
        document.getElementById('cellvaluediv_' + tabName).style.display = 'block';
        tableDetailDivSizes[tabName] = {'status': null};
    }
}

function minimizeOrMaxmimizeTableDetailDiv () {
    var tabName = currentTab;
    if (tabName != 'variant' && tabName != 'gene') {
        return;
    }
    var tableDiv = document.getElementById('tablediv_' + tabName);
    var detailDiv = document.getElementById('detaildiv_' + tabName);
    var detailContainerDiv = document.getElementById('detailcontainerdiv_' + tabName);
    var rightDiv = document.getElementById('rightdiv_' + tabName);
    var drag = document.getElementById('dragNorthSouthDiv_' + tabName);
    var cell = document.getElementById('cellvaluediv_' + tabName);
    var maxHeight = rightDiv.offsetHeight - 10;
    if (tableDetailDivSizes[tabName] == undefined) {
        tableDetailDivSizes[tabName] = {'status': 'both'};
    }
    var stat = tableDetailDivSizes[tabName]['status'];
    if (stat == 'both') {
        tableDetailDivSizes[tabName]['tableheight'] = tableDiv.offsetHeight;
        tableDetailDivSizes[tabName]['detailheight'] = detailDiv.offsetHeight;
    }
    if (stat == 'both') {
        stat = 'tablemax';
    } else if (stat == 'tablemax') {
        stat = 'detailmax';
    } else if (stat == 'detailmax') {
        stat = 'both';
    }
    if (stat == 'tablemax') {
        detailDiv.style.display = 'none';
        drag.style.display = 'none';
        cell.style.display = 'none';
        tableDiv.style.display = 'block';
        tableDiv.style.height = maxHeight + 'px';
        $grids[tabName].pqGrid('option', 'height', maxHeight).pqGrid('refresh');
    } else if (stat == 'detailmax') {
        tableDiv.style.display = 'none';
        drag.style.display = 'none';
        cell.style.display = 'none';
        detailDiv.style.display = 'block';
        detailDiv.style.height = maxHeight + 'px';
        detailDiv.style.top = '10px';
        $(detailContainerDiv).packery();
    } else if (stat == 'both') {
        tableDiv.style.display = 'block';
        detailDiv.style.display = 'block';
        drag.style.display = 'block';
        cell.style.display = 'block';
        var tableHeight = tableDetailDivSizes[tabName]['tableheight'];
        var detailHeight = tableDetailDivSizes[tabName]['detailheight'];
        tableDiv.style.height = tableHeight + 'px';
        $grids[tabName].pqGrid('option', 'height', tableHeight).pqGrid('refresh');
        detailDiv.style.height = detailHeight + 'px';
        detailDiv.style.top = (drag.offsetTop + 10) + 'px';
    }
    tableDetailDivSizes[tabName]['status'] = stat;
    changeTableDetailMaxButtonText();
}
