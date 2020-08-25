```
How to run:
```
make (to build the RooUnfold shared library)

python run_2d/Unfolding.py


```
What it does:
```
This framwork is used for the calculation of the double differential cross sections using the unfolded distributions, the approach used in this analysis consist of transforming the 2D unfolding to 1D unfolding, principally by changing the migration matrix. This framework allows to:

- Make control plots comparing data and simulation:

<img width="689" alt="Screenshot 2020-08-25 at 14 51 58" src="https://user-images.githubusercontent.com/53044514/91176440-9250fd00-e6e2-11ea-91d7-e0db624c1e99.png">

- Changing the 2D unfolding to 1D unfolding:

<img width="714" alt="Screenshot 2020-08-25 at 14 54 10" src="https://user-images.githubusercontent.com/53044514/91176632-db08b600-e6e2-11ea-99a9-ee5f23f0035d.png">

- Calculate the double differential cross sections:

<img width="690" alt="Screenshot 2020-08-25 at 14 55 10" src="https://user-images.githubusercontent.com/53044514/91176731-fd9acf00-e6e2-11ea-82e6-dbed32482e52.png">

