from markdown2 import markdown
import click
import os

@click.command()
@click.option('-i','--input-directory','--input_directory', default = " ", help="Indicate the path of your MarkDown file.")
@click.option('-o','--output-directory','--output_directory', default = " ", help="Indicate the path where you want your HTML to go.")
@click.option('-t','--title', default = "Static Website", help ="Choose your WebSite title. If you dont, it will take a default one (Static Website)")


def ElConvertissore(input_directory,output_directory,title):

    nbr_Md = 1
    directory = os.listdir(input_directory)

    if output_directory == '':
        print("No such output directory choosed")
        quit()
        
    if input_directory == '':
        print("No such input directory choosed")
        quit()
        
    if input_directory[0] == '"' or input_directory[0] == "'":
        print("Wrong format input")
        quit()
    else :
        for i in directory:
            if ".md" in i:
                for j in directory:
                    if ".css" in j:
                        print("Starting conversion ...")
                        mdFile = open(input_directory+"\\"+i, "r", encoding="utf-8")
                        lines = mdFile.readlines()
                        mdFile.close()

                        if not os.path.exists(output_directory):
                            os.makedirs(output_directory)

                        htmlFile = open(output_directory+"\index_n"+str(nbr_Md)+".html", "w", encoding="utf-8")
                        htmlFile.write("<!DOCTYPE html>\n<html>\n<head>\n<title>"+title+"</title>\n<link rel='stylesheet' type='text/css' href='styles.css'>\n</head>\n<body>\n")

                        for l in lines:
                            ligne_convertie = markdown(l)
                            htmlFile.write(ligne_convertie+"\n")

                        htmlFile.write("</body>\n</html>")
                        htmlFile.close()
                        nbr_Md += 1
                        print("Conversion successfully ended !")

                        print("Adding your CSS file ...")
                        mdFile = open(input_directory+"\\"+j, "r", encoding="utf-8")
                        lines = mdFile.readlines()
                        mdFile.close()

                        cssFile = open(output_directory+"\styles.css", "w", encoding="utf-8")

                        for lcss in lines:
                            cssFile.write(lcss+"\n")
                        print("Your CSS file has been successfully added !")
                    else:
                        pass

                print("Starting conversion ...")
                mdFile = open(input_directory+"\\"+i, "r", encoding="utf-8")
                lines = mdFile.readlines()
                mdFile.close()

                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)

                htmlFile = open(output_directory+"\index_n"+str(nbr_Md)+".html", "w", encoding="utf-8")
                htmlFile.write("<!DOCTYPE html>\n<html>\n<head>\n<title>"+title+"</title>\n<link rel='stylesheet' type='text/css' href='styles.css'>\n</head>\n<body>\n")

                for i in lines:
                    ligne_convertie = markdown(i)
                    htmlFile.write(ligne_convertie+"\n")

                htmlFile.write("</body>\n</html>")
                htmlFile.close()
                nbr_Md += 1
                print("Conversion successfully ended !")

                
if __name__ == "__main__":
    ElConvertissore()
