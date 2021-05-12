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

def  get_weight_for_query(query):
    query_freq ={}
    for i in terms:
        if i not in query_freq:
            query_freq.update( { i : 0 } )
    
    for val in query:
        if val in query_freq:
                query_freq[val] += 1
  
    

    for i in query_freq:
        query_freq[i] =  query_freq[i]/4
    
    
    return query_freq
    #return the query vector which is obtained in the boolean form        

def similarity_computation(query_weight):
    numerator =0
    denomi1 = 0
    denomi2 = 0
    similarity ={}
    for document in dicti:
        for terms in dicti[document]:
            numerator += weight[terms] * query_weight[terms]
            denomi1 += weight[terms] * weight[terms]
            denomi2 += query_weight[terms] * query_weight[terms]
        
        if denomi1 !=0  and denomi2 != 0:
            simi = numerator / (math.sqrt(denomi1) * math.sqrt(denomi2))
            similarity.update({document : simi})
            numerator = 0
            denomi2 = 0
            denomi1 =0
    return (similarity)   

def prediction(similarity,doc_count):
    #print(similarity)
    with open('output.txt', 'w') as f:
        with redirect_stdout( f ):
            #to redirect the output to a text file
            ans = max( similarity, key = similarity.get )
            print(ans)

            #print( ans, "is the most relevant document for the given query" )
            #to print the name of the document which is most relevant

            print( "ranking of the documents" )
            for i in range(doc_count):
                ans = max( similarity, key= lambda x: similarity[x])
                print(ans, "rank is", i+1)
                similarity.pop(ans)

            

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

    print("Enter the query")
    query = input()
    #to get the query input from the user, the below input is given for obtaining the output as in output.txt file
    #hockey is a national sport

    query=query.split(' ')
    #spliting the query as a list of strings
    
    query_weight = get_weight_for_query(query)
    #print(query_weight)
    similarity = similarity_computation(query_weight)
    
    prediction(similarity, rows)

main()