from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
from werkzeug.datastructures import MultiDict
from views.forms import EmployeeForm
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = "SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, IF(c.name is not null, c.name,'N/A') AS company_name from IS601_MP2_Employees e LEFT JOIN IS601_MP2_Companies c ON e.company_id = c.id WHERE 1=1"
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]

    allowed_columns_tuples = [(c, c) for c in allowed_columns]

    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    email = request.args.get("email")
    company = request.args.get("company")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)

    # TODO search-3 append like filter for first_name if provided
    if fn:
        query += " AND first_name like %s"
        args.append(f"%{fn}%")

    # TODO search-4 append like filter for last_name if provided
    if ln:
        query += " AND last_name like %s"
        args.append(f"%{ln}%")

    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND email like %s"
        args.append(f"%{email}%")

    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += f" AND company_id = {company}"

    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order:
        print(column, order)
        if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))

    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
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
        # TODO search-10 make message user friendly
        flash(f"Following exception occured while fetching the Employee list: {str(e)}", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns_tuples)

@employee.route("/add", methods=["GET","POST"])
def add():
    form = EmployeeForm(request.form)
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        company_id = request.form.get("company", None)
        # TODO add-2 first_name is required (flash proper error message)
        if first_name == '' or first_name == None:
            flash("first name is required", "danger")
            return redirect("add")
        # TODO add-3 last_name is required (flash proper error message)
        if last_name == '' or last_name == None:
            flash("last name is required", "danger")
            return redirect("add")
        # TODO add-4 company (may be None)
        if company_id == '':
            company_id = None
        # TODO add-5 email is required (flash proper error message)
        if email == '' or email == None:
            flash("email is required", "danger")
            return redirect("add")

        import re
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, email):
            flash("Invalid email", "warning")
            return redirect("add")
        
        try:
            result = DB.insertOne("""
            INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(company_id)s)
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = %(company_id)s
            """, {'first_name': first_name, 'last_name': last_name, 'email': email, 'company_id': company_id}) # <-- TODO add-6 add query and add arguments
            if result.status:
                flash("Created Employee Record", "success")
        except Exception as e:
            # TODO add-7 make message user friendly
            print(e)
            flash(f" Following exception occured while adding the employee record: {str(e)}", "danger")
    return render_template("add_employee.html", form=form)

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    form = EmployeeForm(request.form)
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if id is None:
        flash("ID is missing", "danger")
        return redirect("employee.search")
    else: # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            company_id = request.form.get("company", None)
            # TODO edit-2 first_name is required (flash proper error message)
            if first_name == '' or first_name == None:
                flash("first name is required", "danger")
                return redirect("add")
            # TODO edit-3 last_name is required (flash proper error message)
            if last_name == '' or last_name == None:
                flash("last name is required", "danger")
                return redirect("add")
            # TODO edit-4 company may be None
            if company_id == '':
                company_id = None
            # TODO edit-5 email is required (flash proper error message)
            if email == '' or email == None:
                flash("email is required", "danger")
                return redirect("add")
            
            data = [first_name, last_name, company_id, email]
            data.append(id)
            try:
                # TODO edit-6 fill in proper update query
                result = DB.update("""
                UPDATE IS601_MP2_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s WHERE id = %s
                """, *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-7 make this user-friendly
                flash(f" Following exception occured while updating the employee: {str(e)}", "danger")
        try:
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a copany
            result = DB.selectOne("SELECT e.first_name, e.last_name, e.email, e.company_id, IF(c.name is not null, c.name,'N/A') AS company_name from IS601_MP2_Employees e LEFT JOIN IS601_MP2_Companies c ON e.company_id = c.id WHERE e.id = %s", id)
            if result.status:
                row = result.row
                form.process(MultiDict(row))
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(f" Following exception occured while fetching the updated employee record: {str(e)}", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", form=form, company_id=row['company_id'])

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP2_Employees WHERE id = %s", id)
            if result.status:
                flash("Deleted Employee record", "success")
        except Exception as e:
            flash(f" Following exception occured while deleting the employee record: {str(e)}", "danger")
        del args["id"]
    return redirect(url_for("employee.search", **args))