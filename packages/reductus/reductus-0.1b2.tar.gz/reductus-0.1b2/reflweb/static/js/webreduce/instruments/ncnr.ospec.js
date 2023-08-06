// requires(webreduce.server_api)
webreduce = window.webreduce || {};
webreduce.instruments = webreduce.instruments || {};
webreduce.instruments['ncnr.ospec'] = webreduce.instruments['ncnr.ospec'] || {};

// define the loader and categorizers for ncnr.refl instrument
(function(instrument) {
  function load_ospec(load_params, db, noblock, return_type) {
    // load params is a list of: 
    // {datasource: "ncnr", path: "ncnrdata/cgd/...", mtime: 12319123109}
    var noblock = (noblock == true); // defaults to false if not specified
    var return_type = return_type || 'metadata';
    var calc_params = load_params.map(function(lp) {
      return {
        template: {
          "name": "loader_template",
          "description": "Offspecular remote loader",
          "modules": [
            {"module": "ncnr.ospec.LoadMAGIKPSD", "version": "0.1", "config": {}}
          ],
          "wires": [],
          "instrument": "ncnr.magik",
          "version": "0.0"
        }, 
        config: {"0": {"fileinfo": {"path": lp.path, "source": lp.source, "mtime": lp.mtime}}},
        node: 0,
        terminal:  "output",
        return_type: return_type
      }
    });
    return webreduce.editor.calculate(calc_params, false, noblock).then(function(results) {
      results.forEach(function(result, i) {
        var lp = load_params[i];
        if (result && result.values) {
          result.values.forEach(function(v) {v.mtime = lp.mtime});
          if (db) { db[lp.path] = result; }
        }
      });
      return results;
    });
  }
  
  function make_range_icon(global_min_x, global_max_x, min_x, max_x) {
    var icon_width = 75;
    var rel_width = Math.abs((max_x - min_x) / (global_max_x - global_min_x));
    var width = icon_width * rel_width;
    var rel_x = Math.abs((min_x - global_min_x) / (global_max_x - global_min_x));
    var x = icon_width * rel_x;
    var output = "<svg class=\"range\" width=\"" + (icon_width + 2) + "\" height=\"12\">";
    output += "<rect width=\"" + width + "\" height=\"10\" x=\"" + x + "\" style=\"fill:IndianRed;stroke:none\"/>"
    output += "<rect width=\"" + icon_width + "\" height=\"10\" style=\"fill:none;stroke:black;stroke-width:1\"/>"
    output += "</svg>"
    return output
  }
  
  
  var NEXUZ_REGEXP = /\.nxz\.[^\.\/]+$/
  var NEXUS_REGEXP = /\.nxs\.[^\.\/]+(\.zip)?$/

  instrument.files_filter = function(x) {
    return (
      (NEXUZ_REGEXP.test(x) &&
         (/^(fp_)/.test(x) == false) &&
         (/^rapidscan/.test(x) == false) &&
         (/^scripted_findpeak/.test(x) == false))
    )
  }

  instrument.load_file = load_ospec;
  instrument.default_categories = [
    [["friendly_name"]],
    [["path"]],
    [["polarization"]]
  ];
  instrument.categories = jQuery.extend(true, [], instrument.default_categories);
  
  function add_viewer_link(target, file_objs) {
    var jstree = target.jstree(true);
    var parents_decorated = {};
    var to_decorate = jstree.get_json("#", {"flat": true})
      .filter(function(leaf) { 
        return (leaf.li_attr && 
                'filename' in leaf.li_attr && 
                'source' in leaf.li_attr) 
        })
    // for refl, this will return a list of entries, but
    // we want to decorate the file that contains the entries.
    to_decorate.forEach(function(leaf, i) {
      var parent_id = leaf.parent;
      // only add link once per file
      if (parent_id in parents_decorated) { return }
      var fullpath = leaf.li_attr.filename;
      var datasource = leaf.li_attr.source;
      if (["ncnr", "ncnr_DOI"].indexOf(datasource) < 0) { return }
      if (datasource == "ncnr_DOI") { fullpath = "ncnrdata" + fullpath; }
      var pathsegments = fullpath.split("/");
      var pathlist = pathsegments.slice(0, pathsegments.length-1).join("+");
      var filename = pathsegments.slice(-1);
      var link = "<a href=\"http://ncnr.nist.gov/ipeek/nexus-zip-viewer.html";
      link += "?pathlist=" + pathlist;
      link += "&filename=" + filename;
      link += "\" style=\"text-decoration:none;\">&#9432;</a>";
      var parent_actual = jstree._model.data[parent_id];
      parent_actual.text += link;
      parents_decorated[parent_id] = true;
    })
  }
  
  instrument.decorators = [add_viewer_link];
    
})(webreduce.instruments['ncnr.ospec']);

