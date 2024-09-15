## Property Management
## Contact: [Website KoiERP](https://koierp.com/) or Email [thanhkoierp@gmail.com](mailto:thanhkoierp@gmail.com)

******
![plot](./apartment_management/images/menushow.png)
### Management Apartments, Rental, Rental agency, Entrust and Fees (electric, water, rent, ...etc).
### Include: Tenant Contract, Landlord Contract, Entrust Contract, PM Contract and Maintenance.
### Leasing user screen
![plot](./apartment_management/images/leasing.png)
### Apartment Manager user screen
![plot](./apartment_management/images/pm.png)
### Apartment Screen
![plot](./apartment_management/images/apartment.png)
### Landlord Partner screen
![plot](./apartment_management/images/landlordpartner.png)
### Tenant Partner screen
![plot](./apartment_management/images/tenantpartner.png)
### Landlord contract have two flows:
#### 1. Normal Contract: PM or Entrust contract must be created and status is In progress.
#### 2. Entrust Contract: Entrust contract must be created and status is In progress.
*** 
Tenant contract be signed, the system auto:

    Create Landlord contract.
    Create Commision with Landlord, and deducting commission in Rent cost and Management fee until the full amount of the commission.
    Create Fee Schedule follow Start date and End date include: Rent cost, Management fee, Appartment fee (case apartment available before, require PM contract must In progress)
Leasing user create Deposit and Accounting user create payment follow amount receive.

Leasing user create invoice from Fee Schedule, the system auto:

    Create invoice in Fee Schedule of Landlord contract, PM or Entrust contract follow Start date from Schedule
### Screens
* Tenant contract:

![plot](./apartment_management/images/tenantcontract1.png)
![plot](./apartment_management/images/tenantcontract2.png)
![plot](./apartment_management/images/tenantcontract3.png)
![plot](./apartment_management/images/tenantsch.png)

* Deposit Tenant contract:

![plot](./apartment_management/images/deposit.png)

* Landlord contract:

![plot](./apartment_management/images/landcontract1.png)
![plot](./apartment_management/images/landcontract2.png)
![plot](./apartment_management/images/landcontract3.png)
![plot](./apartment_management/images/landsch.png)
![plot](./apartment_management/images/commissioninv.png)

* PM contract:

![plot](./apartment_management/images/pmcontract1.png)
![plot](./apartment_management/images/pmcontract2.png)
![plot](./apartment_management/images/pmsch.png)

***

#### 2. Entrust Contract: must require Entrust contract (In progress)
*** 
When Tenant contract be signed, the system auto:

    Create Fee Schedule follow Start date and End date include: Rent cost, Management fee, Appartment fee (case apartment available before, require PM contract must In progress)
Leasing user create Deposit and Accounting user create payment follow amount receive.

When Leasing user create invoice from Fee Schedule, the system auto:

    Create invoice in Fee Schedule of Landlord contract, PM or Entrust contract follow Start date from Schedule
***