from Utility import *

G=nx.DiGraph()
parse_graph(G)
draw_graph(G)

prev_sender=-1
send_count=0
receive_count=0

for u,v,d in G.edges(data=True):         
	 current_sender=u
	 current_receiver=v
         send_count=0
         receive_count=0
	 if(current_sender==prev_sender):
	  print "---------------"
          send_count+=1
          print u
	  incoming=0
	  for m,n,t in G.edges(data=True):
	   if(current_sender==n):                   #checking if the sender has received transactions before
             receive_count+=1                    
	     incoming=incoming+float(G[m][n]['BTC']) #calculating total balance of sender 
	     print "Incoming=%f"%incoming
	  a=float(G[current_sender][prev_receiver]['BTC'])
	  b=float(G[current_sender][current_receiver]['BTC']) 
	  print "Outgoing=%f"%(a+b)
	  if(incoming!=0):
	   difference=incoming-(a+b)                 #difference between BTC received and BTC spent
	   print "Difference=%f"%(difference)
           
	   if(difference<0):
	    difference=-(difference)              
	   if(difference<0.001):                     #error margin
            if(a<1 or b<1):                          #matching identities of sender and greater BTC receiver
	     if(b<1):
              print(current_sender+"="+prev_receiver)
              G.remove_edge(current_sender,prev_receiver)
             if(a<1):
              print(current_sender+"="+current_receiver)             
              G.remove_edge(current_sender,current_receiver)
             
	 prev_sender=current_sender
	 prev_receiver=current_receiver
         print "Send_count%d"%send_count
         print "Receive_count%d"%receive_count

draw_graph(G)

