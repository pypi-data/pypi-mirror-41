
window.onload = function () {

    $('#sidebarCollapse').on('click', function () {
        $('#wrapper').toggleClass('sidebar-collapsed');
        if($('#wrapper').hasClass('sidebar-collapsed')){
           localStorage.setItem('sidebarCollapse', true);
        }
        else{
           localStorage.setItem('sidebarCollapse', false);
        }
    });
}


const Main = new function(){

    this.Utils = new function(){

        this.getDateTimeFromTimestamp = function(timestamp){
            var sp = timestamp.split('.');
            var dateTimeString = sp[0]+'/'+sp[1]+'/'+sp[2]+' '+sp[3]+':'+sp[4];
            return dateTimeString
        }

        this.toast = function(type, msg, duration){
            toastr.options = {
                "positionClass": "toast-top-center",
                "timeOut": duration.toString(),
                "hideDuration": "100"
            }
            if(type == 'success')
                toastr.success(msg)
            else if(type == 'error')
                toastr.error(msg)
            else if(type == 'info')
                toastr.info(msg)
        }

        this.displayErrorModal = function(errors){
            var ulContent = '';
            for(e in errors){
                ulContent += "<li>"+errors[e]+"</li>";
            }
            $("#errorList").html(ulContent);
            $("#errorModal").modal("show");
            window.setTimeout(function(){
                $("#errorModal .dismiss-modal").focus();
            }, 500);
        }

        // How to use the confirm modal:
        // Call displayConfirmModal(title, message, callback),
        //
        // When the Confirm Modal is confirmed the callback is called.
        // Pass an anonymous function as callback in order to include parameters with it,
        // example:
        // var callback = function(){
        //     myCustomFunction(param1, param2);
        // }
        this.displayConfirmModal = function(title, message, callback){
            $("#confirmModal .modal-title").html(title);
            $("#confirmModal .modal-body").html(message);
            $("#confirmModal button.confirm").click(function(){
                $("#confirmModal .modal-title").html('');
                $("#confirmModal .modal-body").html('');
                $("#confirmModal button.confirm").unbind('click');
                $("#confirmModal").modal("hide");
                callback();
            })
            $("#confirmModal").modal("show");
            $('#confirmModal').on('shown.bs.modal', function () {
                $("#confirmModal button.confirm").focus();
            });
        }

        // How to use the prompt modal:
        // Call displayPromptModal(title, description, inputValue, callback),
        //
        // When the 'Save' button is clicked, the callback function is called.
        // Pass an anonymous function as callback in order to include parameters with it,
        // example:
        // var callback = function(){
        //     myCustomFunction(param1, param2);
        // }
        this.displayPromptModal = function(title, description, inputValue, inputPlaceholder, callback){
            $("#promptModal .modal-title").html(title);
            $("#promptModal .modal-body .description").html(description);
            $("#promptModal .modal-body input").val(inputValue);

            $("#promptModal").modal("show");
            $('#promptModal').on('shown.bs.modal', function () {
                $('#promptModalInput').focus();
            });

            var sendValue = function(){
                var sentValue = $("#promptModalInput").val();
                callback(sentValue);
                $("#promptModal").modal("hide");
                $("#prompSaveButton").unbind('click');
            }

            $("#promptModal button.confirm").click(function(){
                sendValue();
            })
        }

        // How to use the select prompt modal:
        // Call displaySelectPromptModal(title, description, options, buttonLabel, callback),
        //
        // When the user selects an option from the select, the callback function is called.
        // Pass an anonymous function as callback in order to include parameters with it,
        // example:
        // var callback = function(){
        //     myCustomFunction(param1, param2);
        // }
        this.displaySelectPromptModal = function(title, description, options, buttonLabel, callback){
            buttonLabel = buttonLabel || 'Continue';
            $("#selectPromptModal .modal-title").html(title);
            $("#selectPromptModal .modal-body .description").html(description);

            $("#selectPromptContinueButton").html(buttonLabel);

            $("#selectPromptSelect").html('');
            $.each(options, function(i){
                var itemval = "<option value='"+options[i]+"'>"+options[i]+"</option>";
                $("#selectPromptSelect").append(itemval)
            });
            $("#selectPromptModal button.confirm").focus();
            $("#selectPromptModal").modal("show");
            $('#selectPromptModal').on('shown.bs.modal', function () {
                $("#selectPromptModal button.confirm").focus();
            });
            var confirm = function(){
                var selectedVal = $("#selectPromptSelect").val();
                callback(selectedVal);
                $("#selectPromptModal").modal("hide");
                $("#selectPromptSelect").unbind('change');
                $("#selectPromptSelect").unbind('change');
                $("#selectPromptModal button.confirm").unbind('click');
            }
            $("#selectPromptModal button.confirm").click(function(){
                confirm();
            })
        }

        this.guid = function()  {
            function s4() {
                return Math.floor((1 + Math.random()) * 0x10000)
                    .toString(16)
                    .substring(1);
            }
            return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4();
        }

        this.getResultIcon = function(result){
            let classValue;
            let svg;
            switch(result) {
                case Main.ResultsEnum.pending.code:
                    svg = $(`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>`);
                    break;
                case Main.ResultsEnum.success.code:
                    svg = $(`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" data-reactid="251"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>`)
                    break;
                case Main.ResultsEnum.failure.code:
                    svg = $(`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>`);
                    break;
                case Main.ResultsEnum.error.code:
                    svg = $(`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12" y2="16"></line></svg>`);
                    break;
                case Main.ResultsEnum['code error'].code:
                    svg = $(`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12" y2="16"></line></svg>`);
                    break;
                case Main.ResultsEnum.running.code:
                    // TODO
                    return `<i class="fa fa-cog fa-spin spinner" style=""></i>`
                    break;
                default:
                    svg = $(`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12" y2="17"></line></svg>`);
            }
            svg.css('height', '1em');
            svg.css('width', '1em');
            svg.css('vertical-align', '-0.15em');
            let color = Main.ReportUtils.getResultColor(result);
            let html = $(`<span></span>`).append(svg);
            html.css('color', color);
            return html.get(0).outerHTML
        }

        this.capitalizeWords = function(str){
            return str.replace(/(^|\s)\S/g, l => l.toUpperCase())
        }

        // Displays a dismissable info bar prepended in the container
        this.infoBar = function(container, content){
            let bar = `<div class="info-bar alert alert-info alert-dismissible" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                ${content}
            </div>`;
            container.prepend(bar);
        }

        // incomplete, not used
        this.MultiselectComponent = new function(){

            this._tag = function(value){
                let badge = `<div class="tag label btn md">
                    <span>test</span>
                    <a style="opacity: 0.6;" onclick="this.parentElement.remove()"><i class="remove glyphicon glyphicon-remove-sign glyphicon-white"></i></a>
                </div>`;
                return $(badge)
            }

            this.initialize = function(container, values, id, placeholder){
                let component = `<input type="text" class="form-control" id="${id}" placeholder="${placeholder}">
                                <div class="tag-container"></div>`;
                container.append(component);
                values.forEach(function(value){
                    $(container).find('.tag-container').append(Main.Utils.MultiselectComponent._tag(value))
                })
            }
        }
    }


    this.ReportUtils = new function(){

        this.getResultColor = function(result){
            if(result in Main.ResultsEnum){
                return Main.ResultsEnum[result].color
            }
            else{
                return Main.ReportUtils.colorFromString(result)
            }
        }

        this.colorFromString = function(str){
            let hash = 0;
            if (str.length === 0) return hash;
            for (var i = 0; i < str.length; i++) {
                hash = str.charCodeAt(i) + ((hash << 5) - hash);
                hash = hash & hash;
            }
            hash = Math.abs(hash);
            let hue = hash % 360;
            let s = 50 + hash % 30;
            let l = 40 + hash % 30;
            return `hsl(${hue}, ${s}%, ${l}%)`
        }

        this.createProgressBars = function(container, results){
            results.forEach(function(result){
                let color = Main.ReportUtils.getResultColor(result);
                let bar = $(`
                    <div aria-valuenow='10' style='width: 0%;'
                        class='progress-bar' result-code="${result}"
                        data-transitiongoal='10'>
                    </div>
                `);
                bar.css('background-color', color); 
                container.append(bar);
            });           
        }

        this.expandImg = function(e){
            $("#expandedScreenshot").attr('src', e.srcElement.src);
            $("#screenshotModal").modal('show');
        }

        this.animateProgressBar = function(container, result, percentage){
            setTimeout(function(){
                let bar = container.find(`div.progress-bar[result-code='${result}']`);
                bar.css('width', `${percentage}%`);
            }, 100);
        }

        this.hasProgressBarForResult = function(container, result){
            return container.find(`div.progress-bar[result-code='${result}']`).length != 0
        }
    }

    this.TestRunner = new function(){

        this.testName;
        this.project;
        this.runButton;
        this.defaultBrowser;
        this.supportedBrowsers = [];
        this.projectEnvironments = [];
        this.browsers = '';
        this.environments = '';
        this.processes = 1;

        this.openConfigModal = async function(project, testName){
            Main.TestRunner.project = project;
            Main.TestRunner.testName = testName;
            await Main.TestRunner._getDefaultBrowser()
            if($("#runTestBrowsers").val().length == 0){
                $("#runTestBrowsers").val(Main.TestRunner.defaultBrowser+', ');
            }
            Main.TestRunner._startBrowsersAutocomplete();
            await Main.TestRunner._getProjectEnvironments();
            Main.TestRunner._startEnvironmentsAutocomplete();
            $("#runTestConfigModal").modal("show");
        }

        this.runTest = async function(project, testName){
            Main.TestRunner.project = project;
            Main.TestRunner.testName = testName;
            let projectEnvironments = await Main.TestRunner._getProjectEnvironments();
            if(projectEnvironments.length > 1 && Main.TestRunner.environments.length == 0){
                 Main.TestRunner.openConfigModal(project, testName);
                 $("#runTestConfigModal .info-bar-container").html('');
                 Main.Utils.infoBar($("#runTestConfigModal .info-bar-container"), 'Select at least one environment')
            }
            else{ Main.TestRunner._doRunTestCase() }
        };

        this.runTestFromConfigModal = async function(){
            let error = '';
            Main.TestRunner.browsers = $("#runTestBrowsers").val();
            Main.TestRunner.environments = $("#runTestEnvironments").val();
            let processes = parseInt($("#runTestWorkers").val());
            await Main.TestRunner._getProjectEnvironments();
            if(isNaN(processes)){
                error = 'Workers must be an integer'
            }
            else if(Main.TestRunner.processes < 1){
                error = 'Workers must be at least one'
            }
            else if(Main.TestRunner.projectEnvironments.length > 1 && Main.TestRunner.environments.length == 0){
                error = 'Select at least one environment'
            }
            Main.TestRunner.processes = processes;
            if(error.length > 0){
                Main.TestRunner.openConfigModal(Main.TestRunner.project, Main.TestRunner.testName);
                $("#runTestConfigModal .info-bar-container").html('');
                Main.Utils.infoBar($("#runTestConfigModal .info-bar-container"), error);
            }
            else{
                Main.TestRunner._doRunTestCase();
            }
        };

        this.rerunTest = function(){
            Main.TestRunner._doRunTestCase();
        }

        this._doRunTestCase = function(){
            Main.Utils.toast('info', 'Running test ' + Main.TestRunner.testName, 3000);
            // This is beautiful :O
            // var csvToArray = csvstr => csvstr.length == 0 ? [] : csvstr.split(',').map(item => item.trim());
            var csvToArray = function(csvString){
                if(csvString.length == 0){
                    return []
                }
                else{
                    let items =csvString.split(',').map(item => item.trim());
                    return items.filter(item => item.length > 0)
                }
            }

            $.ajax({
                url: "/run_test_case/",
                data: JSON.stringify({
                     "project": Main.TestRunner.project,
                     "testName": Main.TestRunner.testName,
                     "browsers": csvToArray(Main.TestRunner.browsers),
                     "environments": csvToArray(Main.TestRunner.environments),
                     "processes": Main.TestRunner.processes
                 }),
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                type: 'POST',
                success: function(timestamp) {
                    Main.TestRunner._openResultModal(timestamp);
                 }
             });
        }

        this._openResultModal = function(timestamp){
            $("#runTestConfigModal").modal("hide");
            $("#runModalTestTitle").html(Main.TestRunner.testName);
            $("#testRunModal #testRunModalTabNav").html('');
            $("#testRunModalTabNav").hide();
            $("#testRunModal #TestRunModalTabContainer").html('');
            $("#testRunModal #testRunModalLoadingIcon").show()
            $("#testResults").html('');
            $("#testResultLogs").html('');
            $("#testRunModal").modal("show");
            checkDelay = 1000;
            Main.TestRunner._checkAndRecheckStatus(checkDelay, timestamp);
        }

        this._checkAndRecheckStatus = function(checkDelay, timestamp){
            $.ajax({
                url: "/check_test_case_run_result/",
                data: {
                     "project": Main.TestRunner.project,
                     "testCaseName": Main.TestRunner.testName,
                     "timestamp": timestamp
                },
                dataType: 'json',
                type: 'POST',
                success: function(result) {
                    for (const [setName, values] of Object.entries(result.sets)){
                        Main.TestRunner._updateSet(setName, values, timestamp)
                    }
                    checkDelay += 100;
                    if(result.is_finished){
                        $("#testRunModal #testRunModalLoadingIcon").hide()
                    }
                    else{
                         setTimeout(function(){
                            Main.TestRunner._checkAndRecheckStatus(checkDelay, timestamp);
                        }, checkDelay, Main.TestRunner.project, Main.TestRunner.testName, timestamp);
                    }
                }
            });
        }

        this._getDefaultBrowser = async function(){
            if(Main.TestRunner.defaultBrowser == undefined){
                await $.get('/get_default_browser/', function(defaultBrowser){
                      Main.TestRunner.defaultBrowser = defaultBrowser;
                });
            }
            return Main.TestRunner.defaultBrowser
        }

        this._startBrowsersAutocomplete = async function(){
            if(Main.TestRunner.supportedBrowsers.length == 0){
                await $.get('/get_supported_browsers/', {'project': Main.TestRunner.project}, function(supportedBrowsers){
                      Main.TestRunner.supportedBrowsers = JSON.parse(supportedBrowsers);
                });
            }
            $('#runTestBrowsers').autocomplete({
                lookup: Main.TestRunner.supportedBrowsers,
                minChars: 0,
                delimiter: ', ',
                triggerSelectOnValidInput: false,
                onSelect: function (suggestion) {
                    $('#runTestBrowsers').val($('#runTestBrowsers').val()+', ');
                }
            });
        }

        this._getProjectEnvironments = async function(){
            if(Main.TestRunner.projectEnvironments.length == 0){
                await $.get('/get_environments/', {'project': Main.TestRunner.project}, function(environments){
                      Main.TestRunner.projectEnvironments = JSON.parse(environments);
                });
            }
            return Main.TestRunner.projectEnvironments
        }

        this._startEnvironmentsAutocomplete = function(){
            $('#runTestEnvironments').autocomplete({
                lookup: Main.TestRunner.projectEnvironments,
                minChars: 0,
                delimiter: ', ',
                triggerSelectOnValidInput: false,
                onSelect: function (suggestion) {
                    $('#runTestEnvironments').val($('#runTestEnvironments').val()+', ');
                }
            });
        }

        this._addTabIfDoesNotExist = function(setName){
            let amountOfTabs = $("#testRunModal #testRunModalTabNav .test-run-tab").length;
            let tabExists = $(`.test-run-tab[set-name='${setName}']`).length == 1;
            if(!tabExists){
                let tab = $(`<div role="tabpanel" class="tab-pane test-run-tab-content" id="${setName}" set-name="${setName}">
                                <div class="test-result-logs"></div><div class="test-results"></div>
                             </div>`);
                let tabNav = $(`<li role="presentation" class="test-run-tab" set-name="${setName}" running="true"><a href="#${setName}" aria-controls="${setName}" role="tab" data-toggle="tab">${setName} <i class="fa fa-cog fa-spin"></a></li>`);
                if(amountOfTabs == 0){
                    tab.addClass('active');
                    tabNav.addClass('active');
                }
                else{
                    $("#testRunModalTabNav").show();
                }
                $("#TestRunModalTabContainer").append(tab);
                $("#testRunModalTabNav").append(tabNav);
            }
        }

        this._loadSetReport = function(setName, report, timestamp){
            let reportContainer = $("<div class='report-result'></div>");
            let resultIcon = Main.Utils.getResultIcon(report.result);
            reportContainer.append(`<div class="test-result"><strong>Result:</strong> ${report.result} ${resultIcon}</div>`);
            reportContainer.append('<div><strong>Errors:</strong></div>');
            if(report.errors.length > 0){
                let errorsList = $("<ol class='error-list' style='margin-left: 20px'></ol>");
                report.errors.forEach(function(error){
                    errorsList.append(`<li>${error.message}</li>`);
                });
                reportContainer.append(errorsList);
            };
            reportContainer.append(`<div><strong>Elapsed Time:</strong> ${report.test_elapsed_time}</div>`);
            reportContainer.append(`<div><strong>Browser:<strong> ${report.browser}</div>`);
            reportContainer.append(`<div><strong>Steps:</strong></div>`);
            if(report.steps.length > 0){
                let stepsList = $("<ol class='step-list' style='margin-left: 20px'></ol>");
                report.steps.forEach(function(step){
                    let stepContent = $(`<li>${step.message}</li>`);
                    if(step.error){
                        stepContent.append(' - ' + step.error.message)
                    }
                    if(step.screenshot){
                        let guid = Main.Utils.guid();
                        let screenshotUrl = `/test/screenshot/${Main.TestRunner.project}/${Main.TestRunner.testName}/${timestamp}/${setName}/${step.screenshot}/`;
                        let screenshotIcon = `
                            <span class="cursor-pointer glyphicon glyphicon-picture" aria-hidden="true"
                                data-toggle="collapse" data-target="#${guid}"
                                aria-expanded="false" aria-controls="${guid}"></span>
                            <div class="collapse text-center" id="${guid}">
                                <img class="step-screenshot cursor-pointer" style="width: 100%"
                                    src="${screenshotUrl}" onclick="Main.ReportUtils.expandImg(event);">
                            </div>`;
                        stepContent.append(' ' + screenshotIcon)
                    }
                    stepsList.append(stepContent);
                });
                reportContainer.append(stepsList)
            }
            $(`.test-run-tab-content[set-name='${setName}']>.test-results`).html(reportContainer.html());
            $('.modal-body').scrollTop($('.modal-body')[0].scrollHeight);
        }

        this._updateSet = function(setName, values, timestamp){
            Main.TestRunner._addTabIfDoesNotExist(setName);
            let tab = $(`.test-run-tab-content[set-name='${setName}']`);
            values.log.forEach(function(line){
                let displayedLinesStrings = [];
                tab.find('.test-result-logs div.log-line').each(function(){
                      displayedLinesStrings.push($(this).html())
                 });
                if(!displayedLinesStrings.includes(line)){
                    tab.find('.test-result-logs').append("<div class='log-line'>"+line+"</div>");
                    $('.modal-body').scrollTop($('.modal-body')[0].scrollHeight);
                }
            });
            // If this test set has finished
            if(values.report != null){
                let tabNav = $(`.test-run-tab[set-name='${setName}']`);
                if(tabNav.attr('running') == 'true'){
                    tabNav.removeAttr('running');
                    tabNav.find('i').remove();
                    tabNav.find('a').append(Main.Utils.getResultIcon(values.report.result));
                    Main.TestRunner._loadSetReport(setName, values.report, timestamp);
                }
            }
        }
    }

    this.ResultsEnum = {
        // taken from https://yeun.github.io/open-color/
        'success': {
            code: 'success',
            color: '#37b24d',
        },
        'failure': {
            code: 'failure',
            color: '#f03e3e'
        },
        'error': {
            code: 'error',
            color: '#fd7e14',
        },
        'code error': {
            code: 'code error',
            color: '#fcc419',
        },
        'pending': {
            code: 'pending',
            color: '#74c0fc'
        },
        'running': {
            code: 'running',
            color: '#74c0fc'
        },
        'skipped': {
            code: 'skipped',
            color: '#ced4da'
        },
        'not run': {
            code: 'skipped',
            color: '#868e96'
        }
    }
}