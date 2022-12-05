from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
from werkzeug.datastructures import MultiDict
from views.forms import CompanyForm
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # don't do SELECT *
    query = "SELECT c.id, c.name, c.address, c.city, c.country, c.state, c.zip, c.website, COUNT(e.id) AS Employees from IS601_MP2_Companies c LEFT JOIN IS601_MP2_Employees e ON e.company_id = c.id WHERE 1=1"
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "city", "country", "state"]

    allowed_columns_tuples = [(c, c) for c in allowed_columns]
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)

    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name like %s"
        args.append(f"%{name}%")

    # TODO search-4 append an equality filter for country if provided
    if country:
        query += f" AND country = '{country}'"

    # TODO search-5 append an equality filter for state if provided
    if state:
        query += f" AND state = '{state}'"

    query += " GROUP BY c.id"

    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if column and order:
        print(column, order)
        if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))

    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    try:
        type(int(limit))
    except Exception as e:
        flash("ValueError, the limit entered is not a number", "error")

    if not int(limit) > 0 and int(limit) <= 100:
        flash("Limit entered is out of bounds. Limit should be in between 0 and 100", "error")
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        flash(f"Following exception occured while fetching the company list:{str(e)}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns_tuples)

@company.route("/add", methods=["GET","POST"])
def add():
    form = CompanyForm(request.form)
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = form.name.data
        address = form.address.data
        city = form.city.data
        zipcode = form.zip.data
        website = form.website.data
        state = request.form.get("state", None)
        country = request.form.get("country", None)
        # TODO add-2 name is required (flash proper error message)
        if name == '' or name == None:
            flash("Name is required", "danger")
            return redirect("add")
        # TODO add-3 address is required (flash proper error message)
        if address == '' or address == None:
            flash("Address is required", "danger")
            return redirect("add")
        # TODO add-4 city is required (flash proper error message)
        if city == '' or city == None:
            flash("City is required", "danger")
            return redirect("add")
        # TODO add-5 state is required (flash proper error message)
        if state == '' or state == None:
            flash("State is required", "danger")
            return redirect("add")
        # TODO add-6 country is required (flash proper error message)
        if country == '' or country == None:
            flash("Country is required", "danger")
            return redirect("add")
        # TODO add-7 website is not required
        if website == '':
            website = 'N/A'
        
        has_error = False # use this to control whether or not an insert occurs
        

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                            VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                            ON DUPLICATE KEY UPDATE name=%(name)s, address = %(address)s, city = %(city)s, country = %(country)s, state = %(state)s, zip = %(zip)s, website = %(website)s
                """, {'name': name, 'address': address, 'city': city, 'country': country, 'state': state, 'zip': zipcode, 'website': website}) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash(f" Following exception occured while adding the company: {str(e)}", "danger")
        
    return render_template("add_company.html", form=form)

@company.route("/edit", methods=["GET", "POST"])
def edit():
    form = CompanyForm(request.form)
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if id is None:
        flash("ID is missing", "danger")
        return redirect("company.search")
    else: # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            name = form.name.data
            address = form.address.data
            city = form.city.data
            zipcode = form.zip.data
            website = form.website.data
            state = request.form.get("state", None)
            country = request.form.get("country", None)
            # TODO edit-3 name is required (flash proper error message)
            if name == '' or name == None:
                flash("Name is required", "danger")
                return redirect("add")
            # TODO edit-4 address is required (flash proper error message)
            if address == '' or address == None:
                flash("Address is required", "danger")
                return redirect("add")
            # TODO edit-5 city is required (flash proper error message)
            if city == '' or city == None:
                flash("City is required", "danger")
                return redirect("add")
            # TODO edit-6 state is required (flash proper error message)
            if state == '' or state == None:
                flash("State is required", "danger")
                return redirect("edit")
            # TODO edit-7 country is required (flash proper error message)
            if country == '' or country == None:
                flash("Country is required", "danger")
                return redirect("edit")
            # TODO edit-8 website is not required
            if website == '' or website == None:
                website = 'N/A'
            # 
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            data = [name, address, city, state, country, zipcode, website]
            data.append(id)
            try:
                # TODO edit-9 fill in proper update query
                result = DB.update("""
                UPDATE IS601_MP2_Companies SET name = %s, address = %s, city = %s, state = %s, country = %s, zip = %s, website = %s WHERE id = %s
                """, *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-10 make this user-friendly
                flash(f" Following exception occured while updating the company: {str(e)}", "danger")
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, state, country, zip, website FROM IS601_MP2_Companies WHERE id = %s", id)
            if result.status:
                row = result.row
                form.process(MultiDict(row))
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(f" Following exception occured while fetching the updated company record: {str(e)}", "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", form=form, state=row['state'], country=row['country'])

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP2_Companies WHERE id = %s", id)
            if result.status:
                flash("Deleted Company record", "success")
        except Exception as e:
            flash(f" Following exception occured while deleting the company record: {str(e)}", "danger")
        del args["id"]
    return redirect(url_for("company.search", **args))