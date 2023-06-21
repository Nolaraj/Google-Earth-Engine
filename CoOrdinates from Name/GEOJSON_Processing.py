
import geopandas as gpd
import matplotlib.pyplot as plt
import os
import ntpath



def Single_Conversion(file_name):
    # For Single File Processing
    filepath = r"C:\Users\pnola\Downloads\table.geojson"

    # Read the GeoJSON file
    gdf = gpd.read_file(filepath)

    # Plot the GeoDataFrame
    fig, ax = plt.subplots(figsize=(8, 8))
    gdf.plot(ax=ax)

    # Remove axis labels and ticks
    # ax.set_axis_off()

    # Save the plot as an image file (e.g., PNG)
    plt.savefig(r"C:\Users\pnola\Downloads\table.png", bbox_inches='tight', pad_inches=0)

    # Show the plot (optional)
    plt.show()

    # Read the GeoJSON file
    gdf = gpd.read_file(filepath)

    # Filter the GeoDataFrame based on confidence values
    confidence_threshold = 0.7
    filtered_gdf = gdf[gdf['confidence'] > confidence_threshold]

    # Plot the filtered GeoDataFrame
    fig, ax = plt.subplots(figsize=(8, 8))
    filtered_gdf.plot(ax=ax)

    # Remove axis labels and ticks
    ax.set_axis_off()

    # Save the plot as an image file (e.g., PNG)
    plt.savefig(r"C:\Users\pnola\Downloads\table1.png", bbox_inches='tight', pad_inches=0)

    # Show the plot (optional)
    plt.show()


#For processing Multiple files in the directory
def Multi_Conversions(Folder_Name):
    os.chdir(Folder_Name)
    ext = ('.geojson')

    def OpenFile(filelink):
        f = open(filelink, 'w')
        return f
    def SaveAndReOpen(filelink, fileObj):
        fileObj.close()
        return open(filelink, 'a')

    Textfile = os.path.join(Folder_Name, "Remarks.txt")
    f = OpenFile(Textfile)
    for index, files in enumerate(os.listdir(Folder_Name)):
        if index%5 == 0:
            f = SaveAndReOpen(Textfile, f)
            print(f"Session Saved for file Numbers {index}")


        if files.endswith(ext):
            filename = ntpath.basename(files)
            try:
                gdf = gpd.read_file(files)
                confidence_threshold = 0.7
                filtered_gdf = gdf[gdf['confidence'] > confidence_threshold]
                fig, ax = plt.subplots(figsize=(8, 8))
                filtered_gdf.plot(ax=ax)
                # ax.set_axis_off()
                plt.savefig(f"{filename}.png", bbox_inches='tight', pad_inches=0)

                # Show the plot (optional) and Write the Remarks to file
                def plot_and_show():
                    plt.show()

                def handle_keyboard_interrupt(event):
                    if event.key == 'q':
                        plt.close()

                cid = fig.canvas.mpl_connect('key_press_event', handle_keyboard_interrupt)
                plot_and_show()
                fig.canvas.mpl_disconnect(cid)

                # plt.show()
                remarks = input(f"Enter Shape for plot of {filename} ")
                f.write(filename)
                f.write('\t')
                f.write(str(remarks))
                f.write('\n')
                # plt.close()

            except:
                f.write(filename)
                f.write('\t')
                f.write("NA")
                f.write('\n')

Folder_Name = r"C:\Users\pnola\Documents\Data\College"
Multi_Conversions(Folder_Name)

