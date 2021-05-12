#implementation of boolean model for document retrival

import pandas
#module to read the contents of the file from a csv file

from contextlib import redirect_stdout
#module to redirect the output to a text file

import math

terms = []
#list to store the terms present in the documents

keys = []
#list to store the names of the documents 

vec_dic = {}
#dictionary to store the name of the document and the boolean vector as list

dicti = {}
#dictionary to store the name of the document and the terms present in it as a vector

dummy_list = []
#list for performing some operations and clearing them  

term_freq ={}
idf = {}
weight = {}
def filter( documents, rows, cols ):
    '''function to read and separate the name of the documents and the terms present in it to a separate list  from the data frame and also create a dictionary which 
    has the name of the document as key and the terms present in it as the list of strings  which is the value of the key'''
    for i in range( rows ):
        for j in range( cols ):
            #traversal through the data frame

            if( j == 0 ):
                #first column has the name of the document in the csv file
                keys.append( documents.loc[i].iat[j] )
            else:
                dummy_list.append( documents.loc[i].iat[j] )
                #dummy list to update the terms in the dictionary

                if documents.loc[i].iat[j] not in terms:
                    #add the terms to the list if it is not present else continue
                    terms.append( documents.loc[i].iat[j] )
                
        copy = dummy_list.copy()
        #copying the the dummy list to a different list

        dicti.update( { documents.loc[i].iat[0]:copy } )
        #adding the key value pair to a dictionary

        dummy_list.clear()
        #clearing the dummy list

    #print(dicti)  

def compute_weight( doc_count, cols ):
    for i in terms:
        if i not in term_freq:
            term_freq.update( { i : 0 } )
    
    for key, value in dicti.items():
        for k in value:
            if k in term_freq:
                term_freq[k] += 1
  
    
    idf = term_freq.copy()

    for i in term_freq:
        term_freq[i] =  term_freq[i]/4
    
    for i in idf:
        if idf[i] != doc_count:
            idf[i] = math.log2( 4/ idf[i])
        else:
            idf[i] = 0

    for i in idf:
        weight.update({i : idf[i]*term_freq[i]})
    

    for i in dicti:
        for j in dicti[i]:
            dummy_list.append(weight[j])
              
        copy = dummy_list.copy()
        vec_dic.update({i:copy})
        dummy_list.clear()



    print(term_freq)
    print(idf)
    print(vec_dic)
    
def main():
    documents = pandas.read_csv(r'documents.csv')
    #to read the data from the csv file as a dataframe

    rows = len( documents )
    #to get the number of rows

    cols = len( documents.columns ) 
    #to get the number of columns

    filter( documents, rows, cols )
    #function call to read and separate the name of the documents and the terms present in it to a separate list  from the data frame and also create a dictionary which 
    #has the name of the document as key and the terms present in it as the list of strings  which is the value of the key

    compute_weight(rows, cols )      

main()