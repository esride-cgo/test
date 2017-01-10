## Purpose
Provide assistence to occasional users to deal with Sentinel data in a local ArcGIS Desktop environment by means of two Python Toolbox tools and common ArcGIS Desktop experience:

1. **Search** Data Hub Services' (DHuS) product catalog for Sentinel-2 L1C products according to given criteria.
  ![](doc/Search.png "Search tool results.")
2. Interactively browse metadata (attribute table) and product previews (by selecting product records); mark desired product records for download.
3. With each Marked entry in the local product catalog, **Download** the respective raster data package.
  ![](doc/Download.png "Download in a batch run.")

On download success, the respective raster datasets are presented in ArcMap.

## Prerequisites
* Valid login credentials for DHuS ([self-registration](https://scihub.copernicus.eu/userguide)).
* Tested with ArcGIS Desktop 10.4.1.
* [ArcGIS 10.4.1 Raster Patch](http://support.esri.com/Products/Desktop/arcgis-desktop/arcmap/10-4-1#downloads?id=7396).
* On affected systems: [ArcGIS Runtime Error R6034 Patch](http://support.esri.com/download/7391).

## Getting Started
* [Download ZIP](../../archive/master.zip) and extract its contents to a local folder that can be reached by an ArcGIS _Folder Connection_.  
  📓 Note: Do not simply drag and drop the Toolbox icon to a desired ArcGIS _Folder Connection_ (e.g. "My Toolboxes"), because by doing so ArcGIS Desktop only copies the Toolbox .pyt file in conjunction with the belonging .xml help files but leaves out all other dependend files!
* It is highly advised to read the respectivce _Item Description_ of the Toolbox itself and each tool (see respective context menu), particularly the respective tool _Usage_ of each tool.