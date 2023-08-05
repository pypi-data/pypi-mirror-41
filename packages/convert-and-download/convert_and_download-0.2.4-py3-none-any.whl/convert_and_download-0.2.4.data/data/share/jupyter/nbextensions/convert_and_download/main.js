// Add new exporter

define([
    'jquery',
    'base/js/namespace',
    'base/js/utils'
], function(
    $,
    Jupyter,
    utils
) {
    function load_ipython_extension() {

        var old_selection_changed = Jupyter.NotebookList.prototype._selection_changed;
        Jupyter.NotebookList.prototype._selection_changed = function () {
            var that = this;
            old_selection_changed.call(this);
            var only_notebooks_selected = true;
            var checked = 0;
            $('.list_item :checked').each(function(index, item) {
                var parent = $(item).parent().parent();
                // If the item doesn't have an upload button, isn't the
                // breadcrumbs and isn't the parent folder '..', then it can be selected.
                // Breadcrumbs path == ''.
                if (parent.find('.upload_button').length === 0 && parent.data('path') !== '' && parent.data('path') !== utils.url_path_split(that.notebook_path)[0]) {
                    checked++;
                    // Check that only_notebooks_selected is true and this item is a notebook
                    // The && short-circuits the check if only_notebooks_selected is already false
                    only_notebooks_selected = only_notebooks_selected && parent.data('type') === 'notebook';
                }
            });
            if (checked >= 1 && only_notebooks_selected) {
                $('.convert-download-button').css('display', 'inline-block');
            } else {
                $('.convert-download-button').css('display', 'none');
            }
        };

        convert_and_download = function() {
            var selected = [];
            var url = utils.url_path_join(utils.get_body_data("baseUrl"), 'dlconvert', 'pdf');
            $('.list_item :checked').each(function(index, item) {
                var parent = $(item).parent().parent();
                if (parent.data('type') === 'notebook') {
                    url = utils.url_path_join(url, utils.encode_uri_components(parent.data('path')));
                }
            });
            url = url + '?download=true';
            var w = window.open('', Jupyter._target);
            w.location = url;
        };

        $('<button/>')
            .attr('title', 'Convert and download selected')
            .attr('aria-label', 'Convert and download selected')
            .addClass('convert-download-button btn btn-default btn-xs')
            .text('Convert and download selected')
            .insertBefore('.shutdown-button')
            .css('display', 'none')
            .on('click', convert_and_download);

    };

    return {
        load_ipython_extension: load_ipython_extension
    };
});
