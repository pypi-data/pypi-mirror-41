/**
 *
 */
function load_metadata_with_callback() {

    var url = new URL(window.location.href);
    var id = url.searchParams.get("id");
    //var json_url = document.location.origin + '/reports/' + id
    var json_url = 'http://localhost:8000' + '/reports/' + id

    if(typeof scoutsuite_results == 'undefined'){

        $.getScript(json_url).then(function() {
            load_metadata();
            console.log('Loading Scout Suite done.');
        }).fail(function() {
            console.log('Loading Scout Suite failure.');
            // deal with the failure
        });

    };

}


/**
 * Get the whole config dictionary
 * @returns {{aws_account_id, last_run, metadata, provider_code, provider_name, service_groups, service_list, services, sg_map, subnet_map}|*}
 */
function get_scoutsuite_results() {

    return scoutsuite_results;

}


