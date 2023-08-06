// requires(webreduce.server_api)
webreduce = window.webreduce || {};
webreduce.instruments = webreduce.instruments || {};
webreduce.instruments['ncnr.sans'] = webreduce.instruments['ncnr.sans'] || {};

// define the loader and categorizers for ncnr.sans instrument
(function(instrument) {
  function load_sans(load_params, db, noblock, return_type) {
    // load params is a list of: 
    // {datasource: "ncnr", path: "ncnrdata/cgd/...", mtime: 12319123109}
    var noblock = (noblock == true); // defaults to false if not specified
    var return_type = return_type || 'metadata';
    var calc_params = load_params.map(function(lp) {
      return {
        template: {
          "name": "loader_template",
          "description": "SANS remote loader",
          "modules": [
            {"module": "ncnr.sans.LoadSANS", "version": "0.1", "config": {}}
          ],
          "wires": [],
          "instrument": "ncnr.sans",
          "version": "0.0"
        },
        config: {"0": {"filelist": [{"path": lp.path, "source": lp.source, "mtime": lp.mtime}]}},
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
    })
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

  instrument.load_file = load_sans;
  instrument.default_categories = [
    [["analysis.groupid"]],
    [["analysis.intent"]], 
    [["run.configuration"]], 
    [["run.experimentScanID"],["sample.description"]]
  ];
  instrument.categories = jQuery.extend(true, [], instrument.default_categories);  
  
  function add_sample_description(target, file_objs) {
    var jstree = target.jstree(true);
    //var path = webreduce.getCurrentPath(target.parent());
    var to_decorate = jstree.get_json("#", {"flat": true})
      .filter(function(leaf) { 
        return (leaf.li_attr && 
                'filename' in leaf.li_attr &&
                leaf.li_attr.filename in file_objs &&
                'entryname' in leaf.li_attr &&
                'source' in leaf.li_attr &&
                'mtime' in leaf.li_attr) 
        })
  
    to_decorate.forEach(function(leaf, i) {
      var filename = leaf.li_attr.filename;
      var file_obj = file_objs[filename];
      var entry = file_obj.values.filter(function(f) {return f.entry == leaf.li_attr.entryname});
      if (entry && entry[0]) {
        var e = entry[0];
        if ('sample.description' in e) {
          leaf.li_attr.title = e['sample.description'];
          var parent_id = leaf.parent;
          parent = jstree._model.data[parent_id];
          parent.li_attr.title = e['sample.description'];
        }
      }
    });
  }
  
  
  function add_counts(target, file_objs) {
    var jstree = target.jstree(true);
    var leaf, entry;
    var to_decorate = jstree.get_json("#", {"flat": true})
      .filter(function(leaf) { 
        return (leaf.li_attr && 
                'filename' in leaf.li_attr && 
                leaf.li_attr.filename in file_objs &&
                'entryname' in leaf.li_attr && 
                'source' in leaf.li_attr &&
                'mtime' in leaf.li_attr) 
        })
    
    to_decorate.forEach(function(leaf, i) {
      var filename = leaf.li_attr.filename;
      var file_obj = file_objs[filename];
      var entry = file_obj.values.filter(function(f) {return f.entry == leaf.li_attr.entryname});
      if (entry && entry[0]) {
        var e = entry[0];
        //console.log(e, ('run.detcnt' in e && 'run.moncnt' in e && 'run.rtime' in e));
        if ('run.detcnt' in e && 'run.moncnt' in e && 'run.rtime' in e) {
          var leaf_actual = jstree._model.data[leaf.id];
          leaf_actual.li_attr.title = 't:' + e['run.rtime'] + ' det:' + e['run.detcnt'] + ' mon:' + e['run.moncnt'];
        }
      }
    });
  }
  
  function add_viewer_link(target, file_objs) {
    var jstree = target.jstree(true);
    var to_decorate = jstree.get_json("#", {"flat": true})
      .filter(function(leaf) { 
        return (leaf.li_attr && 
                'filename' in leaf.li_attr && 
                'source' in leaf.li_attr) 
        })
    to_decorate.forEach(function(leaf, i) {
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
      var leaf_actual = jstree._model.data[leaf.id];
      leaf_actual.text += link;
    })
  }
  
  instrument.decorators = [add_viewer_link, add_counts];
    
})(webreduce.instruments['ncnr.sans']);

