# **Import Products From the Inline Source Tutorial**

## Let's get started

The inline importing is a convenient way to make bulk changes in a catalog, such as:

- Import some amount of products, no more than 100 at a time.
- Update products.
- Make fast and frequent changes to the products quantity or price or any other field.

To import your products into a catalog inline you should prepare the **```product_inline_source```** object which is a set
of products. 

Each product should be provided in a JSON format as a standalone line (one product per line with line breaks as a
delimiter). To find an example of a product in JSON format, refer to
the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#json-format)

To find more information about different import types, their restrictions, and use cases, refer to the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations)

**Time to complete**: 
<walkthrough-tutorial-duration duration="3.0"></walkthrough-tutorial-duration>

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and
run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Import products from the inline source

The only reconciliation mode available for inline importing is INCREMENTAL. That is, importing automatically creates new products and updates current products. Products already present in a catalog and missing from the imported JSON source will not change.

To check the example of an import product request, open **product/import_products_inline_source.py**.

The **```parent```** field contains a **catalog name** along with a branch number which you are going to import your
products to.

The **```input_config```** field defines the **ProductInlineSource** as an import source.

To use generated products in this tutorial, check the **```get_products()```** function first.

To perform the products importing, open the Terminal and run the following command:

```bash
python product/import_products_inline_source.py
```

## Response analysis

Once you have called the import products method, the **import operation** has started.

Importing may take some time depending on the size of product set in your inline source.

The operation is completed when the **```operation.done()```** field is set to true.

Check the result, one of the following fields should be present:
 - **```error```**, if the operation failed.
 - **```result```**, if the operation was successful.

You have imported valid product objects into the catalog.

Check the ```import_operation.metadata.success_count``` field to get the total number of the successfully imported products.

The number of failures during the product import is returned in ```import_operation.metadata.failure_count``` field.

## Error handling

Now, let's try to import a few product objects, add an invalid one to them, and check the error message in the operation response. Note that in this case the operation itself is considered as successful.

The title field is a required, so if you remove it, you will get an invalid product object.

Go to the code sample and comment or remove the **```line product1.title = "#IamRemarkable Pen"```** line.

Now, run the code sample and wait till the operation is completed. Check the operation printed out to the Terminal.

## Error hanfling output analysis

The operation is successfully completed, so you can find a **```result```** field. Otherwise, there would be an **```error```** field instead.

Check the error message in the **```result.error_samples```** list. It should state the invalid product object and its field which caused a problem. In our case, the message should be:

```
error_samples {
  code: 3
  message: "Field \"inputConfig.productInlineSource.products.title\" is a required field, but no value is found."
}
```

Next, let's send invalid import request to make the operation fail. 

In the code sample, find the **```get_import_products_inline_request```**  method, and add there a local variable ```default_catalog``` with some invalid catalog name.

Run the code once again and check the error message, it should look like this:

```
google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for importing and import the set amount of
products directly inline.

**Thank you for completing this tutorial!**
