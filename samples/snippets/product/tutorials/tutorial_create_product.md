# **Create Product Tutorial**

## Let's get started

To fill the catalog or to update a massive amount of products we recommend to use import_products method. However
sometimes you may need to make some detached changes in your product catalog. 

For such cases the Retail API provides you such ability
exposing 
 - create_product, 
 - get_product, 
 - update_product,
 - delete_product methods.

In this tutorial you will **create a simple product**.

You can find detailed information about managing catalog information in the [Retail API documentation](https://cloud.google.com/retail/docs/manage-catalog)

**Time to complete**: 
<walkthrough-tutorial-duration duration="2.0"></walkthrough-tutorial-duration>

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

To do that, run the following commands in a terminal:

```bash
python3 -m venv tutorial-env
```

```bash
source tutorial-env/bin/activate
```

Next, install Google packages:

```bash
python3 -m pip install google
```

```bash
python3 -m pip install google.cloud.retail
```

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Product object overview

The required product fields are:

 - **```name```** - Full resource name of the product, which is:
 ```none
 projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>
 ```

 - **```id```** - Product identifier, which is the final component of product name.
 - **```type```** - The type of the product. Default to "PRIMARY"
 - **```primary_product_id```** - Variant group identifier, required for VARIANT products
 - **```categories[]```** - Names of categories the product belongs to, can represent different category hierarchies.
 - **```title```** - The product title which will be to a customer


## Product types overview

There are 3 types of products:

- **```PRIMARY```** - is a simple product which you, as a customer, can think about. From the Retail perspective it is also a
  primary unit for indexing and search serving and predicting. It can be grouped with multiple VARIANT products as a parent product.
- **```VARIANT```** - it is a SKU (Stock keeping unit) -the product item which usually share some common attributes with its parent PRIMARY product, but
  they have variant attributes like different colors, sizes and prices, etc.
- **```COLLECTION```** - it is a product item which groups PRIMARY or VARIANT products that are sold together, such as a jewelry set with necklaces, earrings and rings, etc.

You can get full information about Product object and its fields in
the [Retail API documentation](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)

## Get simple product object

In this tutorial you will create a simple PRIMARY product, like this one, presented in JSON format:

```py
{
  "name": "projects/<PROJECT_NUMBER>/locations/global/catalogs/default_catalog/branches/default_branch/products/<PRODUCT_ID>",
  "id": "PRODUCT_ID",
  "type": "PRIMARY",
  "categories": [
    "Speakers and displays"
  ],
  "brands": [
    "Google"
  ], 
  "title": "Nest Mini",
  "availability": "IN_STOCK",
  "price_info": {
    "price": 30.0,
    "original_price": 35.5,
    "currency_code": "USD"
  }
}
```

Open **create_product.py** code sample and check this product generation with the method ```generate_product()```.

## Create a product in a catalog

To create a product you should send a **CreateProductRequest** to Retail API with the following required fields specified:
 - **```product```** - the product object you want to create
 - **```product_id```** - product id 
 - **```parent```** - a branch name in a catalog where the product will be created

You can find the create product request example in a **create_product.py**

To create a product, open terminal and run the command:

```bash
python product/create_product.py
```

The Retail API returns the created product as a response

## Create a product. Error handling

If you send a request without one of required fields or if the field format is incorrect you will get an error message.

Let's now remove the product field ```name``` and send this request again. The expected error message should be like:

TODO ```[PUT THE ERROR MESSAGE HERE]```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to create a product in a catalog using Retail API. We encourage you to 
practice in creating products right here, in Cloud Shell environment or in your oun Google Cloud Catalog.

**Thank you for completing this tutorial!**
