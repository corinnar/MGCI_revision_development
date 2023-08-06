2. Initial set-up 
===============

2.1 Software Installation 
--------------------------
2.1.1 R software and packages installation

2.1.2 QGIS software and plugins




2.1.1 R software and packages installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download and install R from https://www.r-project.org/ and then
   download and install RStudio Desktop from
   https://www.rstudio.com/products/rstudio/. Once the later has been
   completed, open RStudio in your computer.

2. Click on ‘File’ (top left corner) and then on ‘Open File…’. Select
   the file named ‘XXXXXXXX’ Click on …….to run and install all the
   packages and check that there are no errors.

3. Ensure the ‘sp ‘and ‘raster’ packages are correctly installed. Two of
   the options to do so are:
    -   install.packages("name\_of\_package")
    -  library(name\_of\_package)
    
       Or
    -  (if(!require("name\_of\_package")) install.packages("name\_of\_package")

A step-by-step guide on how to install R and R Studio (with images) can be found in Annex X.
If you are not installing R and R studio from scratch, please make sure that your installations are upgraded. It is important to use the current version of R software (R-4.1.1 at the time of writing). The R version can be easily checked on the text within the ‘R Console’ box at the beginning of a new session (see Figure XX for standalone R and Figure ZZ for R Studio).

|image5|

|image6|

If you are running R on Windows, package ‘installr’ allows you to
quickly update the R version and the packages saved in your library
(please check
https://www.r-statistics.com/2015/06/a-step-by-step-screenshots-tutorial-for-upgrading-r-on-windows/
for a step-by-step tutorial on how to do this or type the lines
bellow on the R Console:

- install.packages("installr") 
    
  *you’ll have to select the CRAN mirror for use in this session depending on your geographical location*

 |image7|
- library(installr)

- updateR()
    
  *Answer the questions to complete the update. The final set of questions are about copying your R packages to the new version of R.*

 |image8|

2.1.2 QGIS software and plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We suggest users use the Long-Term Release version1 [1]_ of QGIS to
undertake their analysis as this is most stable versions and users are
less likely to incur technical difficulties and bugs.

There are various installers depending on your operating system but for
most users we recommend the QGIS Standalone Installer. Full instructions
are on their website
`https://qgis.org/en/site/forusers/download.html# <https://qgis.org/en/site/forusers/download.html>`__

Whilst the MGCI analysis runs entirely within the QGIS interface, users
wishing to use QGIS for the MGCI analysis are also required to install R
software (as outlined above). R scripts can be run from within the QGIS
interface. The R script will be only be used for calculating real
surface area during the MGCI calculation. Real surface area can be
calculated using one of the ready to use SAGA tools in the processing
toolbox, however after initial testing we found the results differed
from the GEE and R methods and therefore due to the need for consistency
between calculation methods for this SDG indicator, the best and easiest
method was to integrate the ‘surfaceArea’ function from package ‘sp in R
software.

Once QGIS and R are both correctly installed users will need to install
the following plugins:

1. **Processing R Provider:** This plugin essentially allows R scripts
   to be used directly within the QGIS processing toolbox with the
   simple addition of some QGIS header information placed at the top of
   the script to making the R script behave exactly like other
   processing tools in the QGIS processing toolbox. The header
   information allows graphical fields to be set in the processing
   dialogue window when running the tool e.g. the input raster, a
   specific field or the location and name of an output raster. Some
   header information is used to tell QGIS to either pass information to
   R and from QGIS about the tool to enable the R processing to happen
   within the QGIS interface.

-  From the QGIS Menu Toolbar click on **Plugins>>Manage and Install
   Plugins**

|image9|

-  From the Plugin dialogue window search for **processing R**

|image10|

-  Click **Install Plugin** and then **Close**

|image11|

|image12|

Once installed R will appear as a processing tool in the processing
toolbox and an R Scripts button in the Processing Toolbox Menu.
Users may find that the R scripts button is missing at this stage.

-  Click the arrow next to the **R** Tools to expand the R toolset.

The toolset should look similar to the below with a few example scripts.

|image13|

and the processing Toolbox Menu should look like this with the missing R scripts button |image14|

|image15|

-  From the QGIS main menu click on **settings>>
   options>>processing>>providers**

-  expand **R** to see the R setting

|image16|

If you operating system is 64 bit, tick **Use 64bit version**

-  Check the **R folder** is pointing to the correct location (where it
   is installed on your computer)

-  Click okay

-  Save the QGIS project and re-open to activate the changes.

You should now see that the R script button has appeared on the
processing toolbox menu

|image17|

Next add additional resources to the R processing toolbox

-  To add other R resources click on **plugins>>resource
   sharing>>resource sharing**

    |image18|

-  Click on **All Collections** on the left hand panel and click **QGIS
   R script collection (QGIS Official Repository)** then click
   **Install**

    |image19|

A wider collection of scripts should now be present in the R-scripts
collection. These are not required for MGCI but useful for R-Integration
with QGIS.

    |image20|
To check that the R integration is correctly installed and
working check that a new script can be created by clicking **‘Create
New R script’** button at the top of the Processing toolbox.

-  Click the **Open Script** button and open the real surface area R
   script that has been adapted to run in QGIS. The file is called
   **RSA\_R\_script\_with\_QGIS\_headers \_final\_v1.rsx** script (to be
   provided)

   |image21|

   The RSA script should open

   |image22|

Note that the script header indicates that the R script will appear
under the **Raster Processing group** in the R toolset in the QGIS
Processing Toolbox, the name of the tool will be **Create RSA raster
v1.**

-  Click the **Save** **script as** button |image23| to save the script
   in your QGIS rscripts folder. Save the script as
   **RSA\_R\_script\_with\_QGIS\_headers\_final\_v1.rsx**

|image24|

-  Click **Save**

-  Add a sample raster (to be provided) to your QGIS project and run the
   following steps to check that the QGIS R-installation is working
   correctly for the RSA script.

|image25|

-  In the Processing Toolbox, double click on the **Create RSA Raster
   V1** tool to open the tool dialogue

    |image26|

|image27|

-  Leave the output to save to a temporary file

-  Click **Run**

    If R has been installed correctly the script should run with no
    errors and an output should be generated which is one cell less in
    all directions compared to the input

-  To make it easier to check the output change the symbology on the
   output to shade **Singleband/Pseudocolor**

|image28|

 The temporary output should look like the below. The reason that the
 layer is one cell less all the way round is that the real surface
 area uses 8 surrounding cells around each cell in the calculation
 and the reason that when processing the data for calculating the
 mountain and real surface area layers that the area of interest
 needs to be defined large than the boundary of the country.

 |image29|

 **Resource sharing plugin:** This plugin is a useful R related
 plugin (which is not essential for the MGCI but useful for users
 wishing to integrate R with QGIS).

 Once the resource sharing plugin is installed some scripts should
 also be visible. They are grouped into several categories as in the
 screengrab below.

 |image30|

 For further information see the following sections of the QGIS user
 manual at

-  https://docs.qgis.org/3.16/en/docs/user_manual/processing/3rdParty.html#r-scripts

-  docs.qgis.org/3.16/en/docs/user\_manual/processing/3rdParty.html#index-5





.. |image0| image:: media_QGIS/image2.png
   :width: 6.26806in
   :height: 3.16875in
.. |image1| image:: media_QGIS/image3.png
   :width: 6.26806in
   :height: 5.06528in
.. |image2| image:: media_QGIS/image4.png
   :width: 6.26806in
   :height: 0.81458in
.. |image3| image:: media_QGIS/image5.png
   :width: 6.26806in
   :height: 1.65347in
.. |image4| image:: media_QGIS/image6.png
   :width: 6.26806in
   :height: 3.97847in
.. |image5| image:: media_QGIS/image7.png
   :width: 5.97917in
   :height: 4.25867in
.. |image6| image:: media_QGIS/image8.png
   :width: 6.03472in
   :height: 4.75909in
.. |image7| image:: media_QGIS/image9.png
   :width: 6.26806in
   :height: 4.46458in
.. |image8| image:: media_QGIS/image10.png
   :width: 6.26806in
   :height: 3.33742in
.. |image9| image:: media_QGIS/image11.png
   :width: 5.52160in
   :height: 0.94805in
.. |image10| image:: media_QGIS/image12.png
   :width: 6.26806in
   :height: 3.70278in
.. |image11| image:: media_QGIS/image13.png
   :width: 4.42770in
   :height: 4.71941in
.. |image12| image:: media_QGIS/image14.png
   :width: 4.42653in
   :height: 4.71816in
.. |image13| image:: media_QGIS/image15.png
   :width: 3.44840in
   :height: 1.83359in
.. |image14| image:: media_QGIS/image16.png
   :width: 0.43750in
   :height: 0.35417in
.. |image15| image:: media_QGIS/image17.png
   :width: 3.21875in
   :height: 1.13542in
.. |image16| image:: media_QGIS/image18.png
   :width: 6.26806in
   :height: 2.56667in
.. |image17| image:: media_QGIS/image19.png
   :width: 2.32263in
   :height: 0.97904in
.. |image18| image:: media_QGIS/image20.png
   :width: 6.26806in
   :height: 3.45417in
.. |image19| image:: media_QGIS/image21.png
   :width: 5.21948in
   :height: 1.75024in
.. |image20| image:: media_QGIS/image22.png
   :width: 1.95347in
   :height: 2.17361in
.. |image21| image:: media_QGIS/image23.png
   :width: 5.10417in
   :height: 1.21875in
.. |image22| image:: media_QGIS/image24.png
   :width: 5.75000in
   :height: 3.93750in
.. |image23| image:: media_QGIS/image25.png
   :width: 0.29861in
   :height: 0.29276in
.. |image24| image:: media_QGIS/image26.png
   :width: 6.26806in
   :height: 3.40417in
.. |image25| image:: media_QGIS/image27.png
   :width: 6.26806in
   :height: 3.59931in
.. |image26| image:: media_QGIS/image28.png
   :width: 3.18056in
   :height: 2.63633in
.. |image27| image:: media_QGIS/image29.png
   :width: 6.26806in
   :height: 2.40000in
.. |image28| image:: media_QGIS/image30.png
   :width: 5.48788in
   :height: 5.13889in
.. |image29| image:: media_QGIS/image31.png
   :width: 5.43750in
   :height: 3.10009in
.. |image30| image:: media_QGIS/image32.png
   :width: 3.37547in
   :height: 4.79234in
.. |image31| image:: media_QGIS/image33.png
   :width: 6.26806in
   :height: 2.66389in
.. |image32| image:: media_QGIS/image34.png
   :width: 5.65728in
   :height: 1.02917in
.. |image33| image:: media_QGIS/image35.png
   :width: 4.00355in
   :height: 1.62431in
.. |image34| image:: media_QGIS/image36.png
   :width: 1.74534in
   :height: 1.62292in
.. |image35| image:: media_QGIS/image37.png
   :width: 5.29167in
   :height: 6.63899in
.. |image36| image:: media_QGIS/image38.png
   :width: 6.28139in
   :height: 0.35833in
.. |image37| image:: media_QGIS/image39.png
   :width: 6.28125in
   :height: 5.64371in
.. |image38| image:: media_QGIS/image40.png
   :width: 5.73024in
   :height: 0.27500in
.. |image39| image:: media_QGIS/image41.png
   :width: 6.26806in
   :height: 5.45486in
.. |image40| image:: media_QGIS/image42.png
   :width: 2.46597in
   :height: 2.24167in
.. |image41| image:: media_QGIS/image43.png
   :width: 6.26806in
   :height: 2.72569in
.. |image42| image:: media_QGIS/image44.png
   :width: 6.26806in
   :height: 6.17639in
.. |image43| image:: media_QGIS/image45.png
   :width: 6.26806in
   :height: 5.56458in
.. |image44| image:: media_QGIS/image46.png
   :width: 6.26806in
   :height: 1.33194in
.. |image45| image:: media_QGIS/image47.png
   :width: 6.26806in
   :height: 2.48403in
.. |image46| image:: media_QGIS/image48.png
   :width: 6.10502in
   :height: 3.58383in
.. |image47| image:: media_QGIS/image49.png
   :width: 4.54167in
   :height: 2.21453in
.. |image48| image:: media_QGIS/image50.png
   :width: 5.50833in
   :height: 3.71962in
.. |image49| image:: media_QGIS/image51.png
   :width: 3.48021in
   :height: 2.14167in
.. |image50| image:: media_QGIS/image52.png
   :width: 5.49984in
   :height: 6.74167in
.. |image51| image:: media_QGIS/image53.png
   :width: 5.50764in
   :height: 2.87097in
.. |image52| image:: media_QGIS/image54.png
   :width: 5.79167in
   :height: 3.75759in
.. |image53| image:: media_QGIS/image55.png
   :width: 5.79572in
   :height: 3.78333in
.. |image54| image:: media_QGIS/image56.png
   :width: 4.08390in
   :height: 1.31268in
.. |image55| image:: media_QGIS/image57.png
   :width: 6.26806in
   :height: 9.07222in
.. |image56| image:: media_QGIS/image58.png
   :width: 3.43128in
   :height: 4.10833in
.. |image57| image:: media_QGIS/image54.png
   :width: 6.26806in
   :height: 4.06667in
.. |image58| image:: media_QGIS/image59.png
   :width: 2.63578in
   :height: 1.68774in
.. |image59| image:: media_QGIS/image60.png
   :width: 5.28584in
   :height: 6.92500in
.. |image60| image:: media_QGIS/image61.png
   :width: 4.97917in
   :height: 0.51042in
.. |image61| image:: media_QGIS/image62.png
   :width: 4.84861in
   :height: 7.35000in
.. |image62| image:: media_QGIS/image58.png
   :width: 3.35417in
   :height: 4.01667in
.. |image63| image:: media_QGIS/image54.png
   :width: 6.26806in
   :height: 4.06667in
.. |image64| image:: media_QGIS/image63.png
   :width: 6.21606in
   :height: 2.15833in
.. |image65| image:: media_QGIS/image64.png
   :width: 2.73125in
   :height: 2.93333in
.. |image66| image:: media_QGIS/image65.png
   :width: 6.26806in
   :height: 5.58958in
.. |image67| image:: media_QGIS/image66.png
   :width: 5.72500in
   :height: 4.53763in
.. |image68| image:: media_QGIS/image67.png
   :width: 5.72500in
   :height: 4.09871in
.. |image69| image:: media_QGIS/image68.png
   :width: 6.26806in
   :height: 6.30417in
.. |image70| image:: media_QGIS/image69.png
   :width: 2.16667in
   :height: 2.37500in
.. |image71| image:: media_QGIS/image70.png
   :width: 3.29167in
   :height: 0.96306in
.. |image72| image:: media_QGIS/image71.png
   :width: 5.73333in
   :height: 4.20440in
.. |image73| image:: media_QGIS/image72.png
   :width: 5.70000in
   :height: 5.32741in
.. |image74| image:: media_QGIS/image73.png
   :width: 6.26806in
   :height: 4.20000in
.. |image75| image:: media_QGIS/image74.png
   :width: 5.83333in
   :height: 9.69306in
.. |image76| image:: media_QGIS/image75.png
   :width: 6.26806in
   :height: 4.29028in
.. |image77| image:: media_QGIS/image76.png
   :width: 5.39167in
   :height: 2.82486in
.. |image78| image:: media_QGIS/image77.png
   :width: 2.50000in
   :height: 1.23056in
.. |image79| image:: media_QGIS/image78.png
   :width: 5.73038in
   :height: 5.49167in
.. |image80| image:: media_QGIS/image79.png
   :width: 2.85556in
   :height: 3.19167in
.. |image81| image:: media_QGIS/image80.png
   :width: 2.65833in
   :height: 1.71265in
.. |image82| image:: media_QGIS/image81.png
   :width: 5.73652in
   :height: 4.69167in
.. |image83| image:: media_QGIS/image82.png
   :width: 6.26806in
   :height: 1.17917in
.. |image84| image:: media_QGIS/image83.png
   :width: 2.64583in
   :height: 1.10417in
.. |image85| image:: media_QGIS/image84.png
   :width: 6.23190in
   :height: 5.26667in
.. |image86| image:: media_QGIS/image85.png
   :width: 2.35625in
   :height: 2.03333in
.. |image87| image:: media_QGIS/image86.png
   :width: 6.26806in
   :height: 5.91944in
.. |image88| image:: media_QGIS/image80.png
   :width: 2.65833in
   :height: 1.71250in
.. |image89| image:: media_QGIS/image87.png
   :width: 5.77619in
   :height: 4.87578in
.. |image90| image:: media_QGIS/image88.png
   :width: 6.26806in
   :height: 4.38403in
.. |image91| image:: media_QGIS/image89.png
   :width: 3.06973in
   :height: 3.67361in
.. |image92| image:: media_QGIS/image90.png
   :width: 6.26806in
   :height: 5.98125in
.. |image93| image:: media_QGIS/image91.png
   :width: 1.62500in
   :height: 1.30208in
.. |image94| image:: media_QGIS/image92.png
   :width: 5.70718in
   :height: 7.59524in
.. |image95| image:: media_QGIS/image93.png
   :width: 6.26806in
   :height: 8.21042in
.. |image96| image:: media_QGIS/image94.png
   :width: 2.14147in
   :height: 0.82576in
.. |image97| image:: media_QGIS/image95.png
   :width: 1.31645in
   :height: 1.62121in
.. |image98| image:: media_QGIS/image96.png
   :width: 1.31509in
   :height: 1.62121in
.. |image99| image:: media_QGIS/image97.png
   :width: 5.78451in
   :height: 5.33333in
.. |image100| image:: media_QGIS/image98.png
   :width: 6.26806in
   :height: 4.53472in
.. |image101| image:: media_QGIS/image99.png
   :width: 6.26806in
   :height: 5.02847in
.. |image102| image:: media_QGIS/image100.png
   :width: 6.26806in
   :height: 5.02986in
.. |image103| image:: media_QGIS/image101.png
   :width: 6.26806in
   :height: 5.02708in
.. |image104| image:: media_QGIS/image101.png
   :width: 6.26806in
   :height: 5.02708in
.. |image105| image:: media_QGIS/image102.png
   :width: 6.26806in
   :height: 5.02847in
.. |image106| image:: media_QGIS/image103.png
   :width: 6.26806in
   :height: 5.24306in
.. |image107| image:: media_QGIS/image104.png
   :width: 6.26806in
   :height: 4.55556in
.. |image108| image:: media_QGIS/image105.png
   :width: 5.97917in
   :height: 4.75366in
.. |image109| image:: media_QGIS/image106.png
   :width: 5.85417in
   :height: 2.86158in
.. |image110| image:: media_QGIS/image107.png
   :width: 6.26806in
   :height: 4.50139in
.. |image111| image:: media_QGIS/image108.png
   :width: 6.26806in
   :height: 5.53472in
.. |image112| image:: media_QGIS/image109.png
   :width: 6.26806in
   :height: 4.48333in
.. |image113| image:: media_QGIS/image110.png
   :width: 6.26806in
   :height: 4.56111in
.. |image114| image:: media_QGIS/image111.png
   :width: 6.26806in
   :height: 4.44792in
.. |image115| image:: media_QGIS/image112.png
   :width: 3.09722in
   :height: 1.37500in
.. |image116| image:: media_QGIS/image113.png
   :width: 6.26806in
   :height: 4.59236in
.. |image117| image:: media_QGIS/image114.png
   :width: 6.26806in
   :height: 4.45694in
.. |image118| image:: media_QGIS/image115.png
   :width: 6.26806in
   :height: 4.60278in
.. |image119| image:: media_QGIS/image116.png
   :width: 6.26806in
   :height: 3.34861in
.. |image120| image:: media_QGIS/image117.png
   :width: 6.26806in
   :height: 6.40000in
.. |image121| image:: media_QGIS/image118.png
   :width: 6.26806in
   :height: 3.95486in
.. |image122| image:: media_QGIS/image119.png
   :width: 6.26806in
   :height: 3.39167in
.. |image123| image:: media_QGIS/image120.png
   :width: 6.26806in
   :height: 5.17708in
.. |image124| image:: media_QGIS/image121.png
   :width: 6.26806in
   :height: 4.38403in
.. |image125| image:: media_QGIS/image122.png
   :width: 6.26806in
   :height: 5.07500in
.. |image126| image:: media_QGIS/image123.png
   :width: 6.26806in
   :height: 5.04306in
.. |image127| image:: media_QGIS/image124.png
   :width: 6.26806in
   :height: 5.04375in
.. |image128| image:: media_QGIS/image125.png
   :width: 6.26806in
   :height: 5.05625in
.. |image129| image:: media_QGIS/image126.png
   :width: 6.26806in
   :height: 5.05208in
.. |image130| image:: media_QGIS/image127.png
   :width: 5.71528in
   :height: 0.77630in
.. |image131| image:: media_QGIS/image128.png
   :width: 5.22222in
   :height: 3.12836in
.. |image132| image:: media_QGIS/image129.png
   :width: 6.26806in
   :height: 1.42500in
.. |image133| image:: media_QGIS/image130.png
   :width: 6.26806in
   :height: 5.07083in
.. |image134| image:: media_QGIS/image131.png
   :width: 6.26806in
   :height: 3.82639in
.. |image135| image:: media_QGIS/image132.png
   :width: 1.74653in
   :height: 1.97917in
.. |image136| image:: media_QGIS/image133.png
   :width: 4.58472in
   :height: 2.31944in
.. |image137| image:: media_QGIS/image134.png
   :width: 6.26806in
   :height: 3.19861in
.. |image138| image:: media_QGIS/image135.png
   :width: 6.26806in
   :height: 6.41458in
.. |image139| image:: media_QGIS/image136.png
   :width: 6.26806in
   :height: 4.29028in
.. |image140| image:: media_QGIS/image137.png
   :width: 6.10208in
   :height: 3.16513in
.. |image141| image:: media_QGIS/image138.png
   :width: 6.10208in
   :height: 3.16056in
.. |image142| image:: media_QGIS/image139.png
   :width: 6.13889in
   :height: 0.51146in
.. |image143| image:: media_QGIS/image140.png
   :width: 6.14021in
   :height: 4.06549in
.. |image144| image:: media_QGIS/image141.png
   :width: 6.13092in
   :height: 1.95833in
.. |image145| image:: media_QGIS/image142.png
   :width: 6.13869in
   :height: 1.52778in
.. |image146| image:: media_QGIS/image143.png
   :width: 1.38205in
   :height: 0.21154in
.. |image147| image:: media_QGIS/image144.png
   :width: 3.60467in
   :height: 2.18781in
.. |image148| image:: media_QGIS/image145.png
   :width: 5.75000in
   :height: 4.76172in
.. |image149| image:: media_QGIS/image146.png
   :width: 5.71528in
   :height: 4.75941in
.. |image150| image:: media_QGIS/image147.png
   :width: 5.70139in
   :height: 4.76269in
.. |image151| image:: media_QGIS/image148.png
   :width: 6.02167in
   :height: 4.97986in
.. |image152| image:: media_QGIS/image149.png
   :width: 5.70833in
   :height: 4.72891in
.. |image153| image:: media_QGIS/image150.png
   :width: 5.93833in
   :height: 4.95903in
.. |image154| image:: media_QGIS/image151.png
   :width: 5.99042in
   :height: 5.01112in
.. |image155| image:: media_QGIS/image152.png
   :width: 6.00084in
   :height: 4.91735in
.. |image156| image:: media_QGIS/image153.png
   :width: 6.26806in
   :height: 2.67639in
.. |image157| image:: media_QGIS/image154.png
   :width: 6.26806in
   :height: 4.40000in
.. |image158| image:: media_QGIS/image155.png
   :width: 5.43001in
   :height: 2.79001in
.. |image159| image:: media_QGIS/image156.png
   :width: 5.07668in
   :height: 3.08334in
.. |image160| image:: media_QGIS/image157.png
   :width: 2.07279in
   :height: 0.21970in
.. |image161| image:: media_QGIS/image158.png
   :width: 6.26806in
   :height: 4.84861in
.. |image162| image:: media_QGIS/image159.png
   :width: 6.26806in
   :height: 4.88403in
.. |image163| image:: media_QGIS/image160.png
   :width: 6.26806in
   :height: 4.86875in
.. |image164| image:: media_QGIS/image161.png
   :width: 6.26806in
   :height: 4.86875in
.. |image165| image:: media_QGIS/image162.png
   :width: 6.26806in
   :height: 4.89653in
.. |image166| image:: media_QGIS/image163.png
   :width: 6.26806in
   :height: 6.27569in
.. |image167| image:: media_QGIS/image164.png
   :width: 5.33408in
   :height: 5.05279in
.. |image168| image:: media_QGIS/image165.png
   :width: 6.26806in
   :height: 4.42014in
.. |image169| image:: media_QGIS/image166.png
   :width: 6.26806in
   :height: 1.02222in

