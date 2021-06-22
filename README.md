# Analysis of Smart Industry Market in Fourth Industries

## Background
- Based on core technologies of the 3rd Industrial Revolution such as ICBM (Iot, Cloud, Big Data, Mobile), the new economic and social paradigm is presented as the 4th Industrial Revolution by converging the real world with the virtual world.
- The definition of core technologies of the Fourth Industrial Revolution in Korea is Iot, Cloud, Big Data, Mobile, AI, Blockchain, 3D printing, Robotics, virtual augmented reality.

## Propose
- We would like to confirm the implementation of smart home, smart factory, smart city, smart medical, and electronic government by combining various industries with ICT technology.
- To verify the connectivity and convergence of technologies, we want to define the weight of the edge according to connectivity by making CPC* a professionally divided technology classification table as node, verifying connectivity, and configuring CPC * CPC Matrix.

## Dataset
- Data Source: USPTO 
- Collecting Data: Patent Number, CPC
- Keywords used to collect: smart home, smart factory, smart city, smart healthcare, e-government
> Data Collected <br/>

![Data Collected](https://user-images.githubusercontent.com/63955072/122854219-57ddde00-d34e-11eb-860e-fc8194bb3c37.png)

## Method
- To determine convergence of CPC by converting Patent_number * CPC matrix to CPC * CPC matrix (2-mode --> 1-mode) (CPC co-occurrence)
- Compare using Gephi for 3 periods (2012–2014/2015-2017/2018–2020)
- Identify key influences within the CPC with Degree Centrality.
- Compare with Node, Edge, components, Density, Inclusiveness, Centralization, etc. to derive interpretation from differences.

## Analysis
- Network Analysis (2012-2014)

![Network Analysis (2012-2014)](https://user-images.githubusercontent.com/63955072/122854776-316c7280-d34f-11eb-8725-1505577a0daa.png)

- Network Analysis (2015-2017)

![Network Analysis (2015-2017)](https://user-images.githubusercontent.com/63955072/122854800-3df0cb00-d34f-11eb-8856-c976c07ae1b4.png)

- Network Analysis (2018-2020)

![Network Analysis (2018-2020)](https://user-images.githubusercontent.com/63955072/122854838-4812c980-d34f-11eb-9c1e-bf1e4ad82b10.png)

- Network Analysis
> Increase the number of Node and Edge. <br/>
> As the number of Average Degree increases, technologies are seen converging. <br/>
> Increasing Degree Centralization allows for increased centralization. <br/>
> The decreasing value of Density indicates that the number of nodes increases and is less dense than convergence. <br/>
> Component Ratio values existed, but patents since 2015 confirm that they are all linked to each other. <br/>

![Network Analysis](https://user-images.githubusercontent.com/63955072/122854975-7abcc200-d34f-11eb-9c0b-17b119da7273.PNG)

## Conclusion
- We can see a surge in related technologies and converging industries since 2017, the beginning of the fourth industry.
- Average Degree, Degree Centralization grows over time to see the convergence of different industries in the Smart industry.
- Prior to the Fourth Industrial Revolution, renewable energy management and video VOD industries had a high proportion, but now wireless network security and management are important and energy efficiency are important.
- Overall, we understand the trends of smart industries in the 4th industry.

