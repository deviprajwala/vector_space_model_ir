# vector_space_model_ir

Information retrieval (IR) is finding material (usually documents) of an unstructured nature, that satisfies an information need from within large collections.The retrieval in this type 
of model is accomplished by assigning non-binary weights to index terms in queries and documents .These term weights are ultimately used to compute the degree of similarity between each 
document stored in the system and the user query.

The query and the documents are represented in the form of vectors and the similarity is calculated based on the cosine of angle between these two vectors.Tf-idf schemes is used for the 
weight calculation which term frequency and inverse document frequency.Here the term frequency means the ratio number of times the  particular term occurs in the document to the maximum 
occurrence of the term, and the inverse document frequency is the log of ratio of total number of documents to the documents containing the particular term.the weight calculated is the 
product of the term frequency and inverse document frequency.

The repositary consists of the program which is the implementation of the vector space model, a csv file which is taken as the input to calculate the weight for the documents, a text 
file which contains the output of the program like the document which is most relevant and the ranking according to the relevance.

Initially we read and separate the name of the documents and the terms present in it to a separate list  from the data frame and also create a dictionary which has the name of the 
document as key and the terms present in it as the list of strings  which is the value of the key ,later we compute the weight for each of the terms in the document. Here the weight is 
calculated with the help of term frequency and inverse document frequency. Once we get the query input from the user, we split the query as a list of strings and get the weight for each 
terms present in the query, here we consider the term frequency as the weight of the terms and then we calculate the similarity measure in which the weight of the query and the document 
is multiplied in the numerator and the weight is squared and squareroot is taken the weights of the query and document. Finally prediction is made regarding the document which is 
relevant.

Reference: Modern information retrieval by Ricardo Baeza-Yates, Berthier Ribeiro-Neto    
