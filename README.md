# LeadScoringML

Lead Scoring Business Analytics Tools

About

Python program designed to cluster historical wins (weddings business) into 5 different customer segments. Each customer is segmented using three data points:

1.	Budget
2.	Number of wedding guests
3.	Days until wedding

Once historical wins customer segments are established, the program inserts a lead, one at a time, and reruns the clustering algorithm to group the lead into one of five clusters. Leads are then printed on a new excel spreadsheet with their corresponding Deal ID, parameters, and cluster number. 

Program Flow

 
Program takes historical wins spreadsheet and sales pipeline spreadsheet as inputs, and outputs a third spreadsheet with corresponding clusters. 

Interpreting Clusters

 
In the above text box, the cluster number is y-axis and the customer parameters are the x-axis. The numbers corresponding to each cell are the average number corresponding to each cluster, with an average of 1 and standard deviation of 0 for each. To further clarify, each number is on a scale from -1 to 1. Given this, segment 0 represents a customer segment with the highest budget, guest count, and days to the wedding. Segment 4 represents a customer segment with a high willingness to pay for a smaller guest count. 

Instructions for Running

1.	To run the program, organize the 3 spreadsheets and the python program into the same folder: 
2.	Navigate to the folder in terminal (if using a Mac).  
3.	Run the program using the following command: 
4.	Leads with clusters are now populated in “DataOutputPipeline.xlsx” 


