path = "E:/"
file_name_1 = paste(path, "pcsv.csv", sep="")
df = read.csv(file_name_1)
plot(X1~X1,df)
