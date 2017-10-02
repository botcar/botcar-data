
var remoteDataUrl = "https://raw.githubusercontent.com/botcar/botcar-data/master/Michaux2017/michaux_specimens_master.tsv"
//var remoteDataUrl = "http://localhost:8000/michaux_specimens_master.tsv"

//var remoteDataUrl = "https://raw.githubusercontent.com/botcar/botcar-data/master/Michaux2017/michaux_test.tsv"
var idParam = "URN"

//var baseUrl = "http://localhost:8000/web-presentation2/index.html"
var baseUrl = "http://folio.furman.edu/projects/botanicacaroliniana/michaux/index.html"
var previewImageUrl1 = "http://www.homermultitext.org/iipsrv?OBJ=IIP,1.0&FIF=/project/homer/pyramidal/deepzoom/"
var previewImageUrl2 = ".tif&wid=200&CVT=JPEG"
var ictUrl = "http://www.homermultitext.org/botcar-images/index.html?urn="

var searchParams = new URLSearchParams(window.location.search);
var filterId = searchParams.get(idParam);

var totalResults = 0;
var showingResults = 0;

function makeImageUrl(urn){
	 var imgUrl = ictUrl + urn;
    return imgUrl; 
}

function makeThumbUrl(urn){
		var imagePath = urn.split(":")[2] + "/" +  urn.split(":")[3].split(".")[0] + "/" + urn.split(":")[3].split(".")[1] + "/";
				imagePath += urn.split(":")[4];
		var imgUrl = previewImageUrl1 + imagePath + previewImageUrl2 ;
		return imgUrl;
}

$( document ).ready(function() {

	url = remoteDataUrl;

   Papa.parse(url, {
		download: true,
			delimiter: "",	// auto-detect
			newline: "",	// auto-detect
			quoteChar: '"',
			header: true,
			dynamicTyping: false,
			preview: 0,
			encoding: "",
			worker: true,
			comments: false,
			step: undefined,
			complete: function(results, file) {
				   console.log("downloaded.");
					if ( filterId ){
						var filteredResults = $.grep(results.data, function(e){ return e[idParam] === filterId ; });
						totalResults = results.data.length;
						showingResults = filteredResults.length;
						generateElements(filteredResults);
					} else {
						totalResults = results.data.length;
						showingResults = results.data.length;
						doTabulator(results.data);
					}
			},
			error: undefined,
			download: true,
			skipEmptyLines: false,
			chunk: undefined,
			fastMode: undefined,
			beforeFirstChunk: undefined,
			withCredentials: undefined
	});

});

function showInfo(total, showing){
	var infoDiv = document.createElement("div");
	$(infoDiv).addClass("infoDiv");
	var infoString = "Showing " + showing + " out of " + total + "."; 
	if (total > showing){
		infoString += " <a href='" + baseUrl + "'>Show All</a>";
	}
	$(infoDiv).html(infoString);
	$("div#dataDiv").append(infoDiv);
}

function doTabulator(results){
	console.log("Doing tabulator");

	//create Tabulator on DOM element with id "example-table"
	$("#bcdata-table").tabulator({
  		 //movableRows: true, //enable user movable rows
	    height:"65%", // set height of table (optional)
	    fitColumns:false, //fit columns to width of table (optional)
			columns:[
				{title:"URN", field:"URN", variableHeight:true, sorter:"string", align:"left", sortable:true, formatter:function(cell, formatterParams){
					var value = cell.getValue();
					return "<a class='imageLink' href='" + baseUrl + "?URN=" + value + "'>" + value + "</a>";		
				}},
				{title:"Image URN", field:"ImageURN", variableHeight:true, sorter:"string", align:"left", sortable:true, formatter:function(cell, formatterParams){
					var value = cell.getValue();
					var returnContents = imageLinks(value);
					return returnContents 
				}},
				{title:"Volume", field:"Volume", headerFilter:true, variableHeight:true, sorter:"string", align:"left", sortable:true},
				{title:"Sheet", field:"Sheet", variableHeight:true, headerFilter:true, sorter:"string", align:"left", sortable:true},
				{title:"Version", field:"VersionName", variableHeight:true, headerFilter:true, sorter:"string", align:"left", sortable:true},
				{title:"Family", field:"Family", variableHeight:true, headerFilter:true, sorter:"string", align:"left", sortable:true},
				{title:"Michaux Name", field:"Michaux Name", variableHeight:true, headerFilter:true, sorter:"string", align:"left", sortable:true},
				{title:"Modern Name", field:"Modern Name", variableHeight:true, headerFilter:true, sorter:"string", align:"left", sortable:true}, 
				{title:"Location", field:"Location", variableHeight:true, headerFilter:true, sorter:"string", align:"left", sortable:true},
				{title:"Annotations", field:"Annotations", headerFilter:true, variableHeight:true, sorter:"string", align:"left", sortable:true},	
				{title:"Type", field:"Type", variableHeight:true, headerFilter:true, sorter:"string", align:"left", sortable:true},
				{title:"Linnaean Class", field:"Linnaean Class", headerFilter:true, variableHeight:true, sorter:"string", align:"left", sortable:true},
				{title:"Linnaean Genus", field:"Linneaen Genus", headerFilter:true, variableHeight:true, sorter:"string", align:"left", sortable:true},
				{title:"Linnaean Order", field:"Linnaean Order", headerFilter:true, variableHeight:true, sorter:"string", align:"left", sortable:true},
				{title:"Flora", field:"Flora", sorter:"string", headerFilter:true, variableHeight:true, align:"left", sortable:true}
			],
			/*
	    rowClick:function(e, id, data, row){ //trigger an alert message when the row is clicked
	        alert("Row " + id + " Clicked!!!!");
	    },
	    */
	});

	//load sample data into the table
	$("#bcdata-table").tabulator("setData", results);

	$("div#dataDiv").removeClass("waiting");
}

function imageLinks(urn){
	if (urn){
		var idStr = urn;
		var thumbElement = "<span id='img_" + idStr.replace(/[:.]/g,"") + "' data-urn='" + urn + "' onClick='" + "kwikImg(this)'> [Quick View] </span>";
		var imageUrl = makeImageUrl(urn);
		return "<a class='imageLink' target='_blank' href='" + imageUrl + "' >" + urn + "</a>";
	} else { return "undefined"; }
 }

function  kwikImg(myElement) {
	var imgId = myElement.id;
	//var newImg = document.createElement("img");
	var urn = $("#" + imgId).data("urn");
	var url = makeThumbUrl(urn);
	var imgSrc = "<img src='" + url + "'></img>";
	$("#" + imgId).html(imgSrc);
	$("#" + imgId).parent().css("height", "auto");
	//$("#" + imgId).parent().css("vertical-align", "middle");
}

/**
columns:[
{title:"URN", field:"URN", sorter:"string", align:"left", sortable:true},
{title:"Image URN", field:"ImageURN", sorter:"string", align:"left", sortable:true},
{title:"Volume", field:"Volume", sorter:"string", align:"left", sortable:true},
{title:"Sheet", field:"Sheet", sorter:"string", align:"left", sortable:true},
{title:"Version", field:"VersionName", sorter:"string", align:"left", sortable:true},
{title:"Family", field:"Family", sorter:"string", align:"left", sortable:true},
{title:"Michaux Name", field:"Michaux Name", sorter:"string", align:"left", sortable:true},
{title:"Modern Name", field:"Modern Name", sorter:"string", align:"left", sortable:true}, 
{title:"Location", field:"Location", sorter:"string", align:"left", sortable:true},
{title:"Annotations", field:"Annotations", sorter:"string", align:"left", sortable:true},	
{title:"Field", field:"Field 2", sorter:"string", align:"left", sortable:true},
{title:"Type", field:"Type", sorter:"string", align:"left", sortable:true},
{title:"Linnaean Class", field:"Linnaean Class", sorter:"string", align:"left", sortable:true},
{title:"Linnaean Genus", field:"Linneaen Genus", sorter:"string", align:"left", sortable:true},
{title:"Linnaean Order", field:"Linnaean Order", sorter:"string", align:"left", sortable:true},
{title:"Flora", field:"Flora", sorter:"string", align:"left", sortable:true}
],
**/

function generateElements2(results){
	showInfo(totalResults, showingResults);
	var heads = Object.keys(results[0]);
	heads.forEach(function(h){
		var newP = document.createElement("p");		
		$(newP).html(h);
		$("div#dataDiv").append(newP);
	});
	results.forEach(function(r){
		var newDiv = document.createElement("div");
		$(newDiv).addClass("recordDiv");
		var keys = Object.keys(r);
		keys.forEach(function(k) {
			var newP = document.createElement("p");		
			$(newP).html(r[k]);
			$("div#dataDiv").append(newP);
		});
	});
	console.log("done parsing.");
	$("div#dataDiv").removeClass("waiting");
}

function generateElements(results){

	showInfo(totalResults, showingResults);

	results.forEach(function(r){


		var newDiv = document.createElement("div");
		$(newDiv).addClass("recordDiv");
		var keys = Object.keys(r);
		keys.forEach(function(k) {
			var fieldDiv = document.createElement("div");
			$(fieldDiv).addClass("fieldDiv");
			var fieldLabel = document.createElement("span");
			$(fieldLabel).addClass("fieldLabel");
			var fieldData = document.createElement("span");
			$(fieldData).addClass("fieldData");
			if (k == "ImageURN"){
				var urn = r[k];
				var imagePath = urn.split(":")[2] + "/" +  urn.split(":")[3].split(".")[0] + "/" + urn.split(":")[3].split(".")[1] + "/";
				imagePath += urn.split(":")[4]
				var imageElement = "<a  href='" + ictUrl + urn + "'><img class='thumbView' src='";
				imageElement += previewImageUrl1 + imagePath + previewImageUrl2 + "'/></a>";
				$(fieldLabel).html(imageElement);
			}  else {
				$(fieldLabel).text(k);
			}
         if (k == idParam ){
				var urn = r[k];
				var specLink = "<a class='imageLink' href='" + baseUrl + "?" + idParam + "=" + r[k] + "'>" + r[k] + "</a>";
				$(fieldData).html(specLink);
			} else {
				$(fieldData).text(r[k]);
			}
			$(fieldDiv).append(fieldLabel);
			$(fieldDiv).append(fieldData);
			$(newDiv).append(fieldDiv);
		});
		$("div#dataDiv").append(newDiv);
	});	
	console.log("done parsing.");
	$("div#dataDiv").removeClass("waiting");
}

