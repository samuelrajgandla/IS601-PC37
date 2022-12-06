<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Samuel Raj Gandla (sg2434)</td></tr>
<tr><td> <em>Generated: </em> 12/6/2022 9:44:39 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/sg2434" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205852839-b7733b5a-1478-44a5-bd13-17f309344870.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated with my UCID , displayed the required message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205856798-8e6e322e-9fbb-4cca-81d2-8cbbc32868fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Empty table for companies in DB extension of vs code/IDE<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205858064-61a2af3b-8249-4b7a-a02e-a24da83837c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Empty table for employees in DB extension of vs code/IDE<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205861857-4315590a-1a24-478f-8da0-6831fb43a995.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code has rejected the non .csv file from uploading.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205861857-4315590a-1a24-478f-8da0-6831fb43a995.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code has rejected the non .csv file from uploading.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205862390-b4edc7c0-1764-4633-81cd-b121672454c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot with the successful upload of the company and employee list. With the<br>number of data uploaded.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205863939-7b927c57-29a8-4616-8a6d-f169c6e61e24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of company data list.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205864272-83e0caac-cf20-4bab-9a32-1754a50a492a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of employees data list.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205906875-3262e407-b010-4a0a-bbe0-d52437bd8f25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing some employee data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205907569-c0e39412-dfd7-4540-8d58-7e9b73fae1e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing some company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205909785-8f1d8ad6-6a28-4c60-8aef-52504d30f51a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML file of add employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205910275-573b568e-c786-437e-b273-66eab46db68a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name, last_name, company (id), email and few are in this screenshot.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205910585-037bb600-306c-4ac7-af63-1594b1baf06c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This contains friendly message flashed and a print() of the exception.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205910919-62734d16-4c89-4c91-bb00-63090717dc5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This contains one of the flash message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205911199-47c89a13-d8c2-4c33-a0c2-b66f5b0c0071.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The first_name and Last_name with the proper flash message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205911513-2d37955b-ba37-4a87-9656-e31715e91b82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Final query of this code.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205862390-b4edc7c0-1764-4633-81cd-b121672454c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message after adding.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205913327-a899d17c-66b0-4176-bbf6-4faa01921b1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It has first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205913515-f39176b1-c082-4f1e-ac6b-f31b1a5e945e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It has last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205913707-75f804f7-899e-4914-997a-42176ab41838.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows error message for email.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205921754-eda13751-b06b-406d-8064-251a90b543ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Final list of employee.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205915654-dff90932-1f43-4886-832e-a61eb765a498.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>list of employee in html.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205906875-3262e407-b010-4a0a-bbe0-d52437bd8f25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee table.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205916529-c197f32f-f0c0-4fdb-b571-dec638c8f621.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append like filter for first_name <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205917258-fd2e193f-4f3e-43e6-9885-d0babcb4f52f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append like filter for last_name <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205917477-465f3247-ce67-485c-87df-87cd16c2de95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append equality filter for company_id <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205917732-25e43360-ca56-4a93-908f-8128262ff63c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append equality filter for email.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205918444-bf249d50-cf2d-49a5-8d53-efd589d60b03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>continuation of the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205918725-1637e7dd-317e-4c87-ba22-64716142b868.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>final part of the code.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205864272-83e0caac-cf20-4bab-9a32-1754a50a492a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output with the required filters applied.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205919942-64003ca7-36fd-45ca-b63e-5e015468362f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code screenshots with required changes<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205920464-e31c7865-3e77-4957-826c-db5806259c7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code with flash message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205864272-83e0caac-cf20-4bab-9a32-1754a50a492a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before the data edit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205921754-eda13751-b06b-406d-8064-251a90b543ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after the edit.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205906875-3262e407-b010-4a0a-bbe0-d52437bd8f25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before the edit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205922596-a4351d45-4200-45ad-ab04-bf12ad7a977e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After the edit.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205923192-cd221ecd-eb86-42ae-9cb1-a649f79ea116.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code of html<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205923804-88726f74-f2f5-4900-83a5-0c298e46faa6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name , address  (flash proper error message) start point of code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205924177-b3b21172-6564-4585-9990-19383ce520a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>continuation with the city and others<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205924450-cfc75c79-2389-4498-b839-fd3f7be0d73d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>continuation of the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205924664-bfcb338e-31b0-4b92-b271-47d0e1b9d4bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this has the input of country.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205924936-543d06e3-1c17-4f33-9b49-df0de44c2dd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>query part of the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205925155-e1acb92a-28a8-4219-968a-f09b8c0d3dda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>end part of the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205926967-b8943143-c2ac-43b2-abd3-c79c42261176.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message of update.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205927815-749f822f-327a-4e9a-bc8e-f97a2db13fdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205928220-11dec5f4-159d-4b70-9d0c-2147102c7c7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>city error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205928493-221ceb5a-5b35-4389-bf2b-e55203e39a6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205928323-04dd0b4f-1aee-45dd-ada9-d961fa512844.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>country error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205928093-0f8d22f3-d7d1-442d-b1b0-df557c779614.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205929279-f50e0a2d-5f82-4f67-b2eb-a43beec7eca7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edited data<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205923804-88726f74-f2f5-4900-83a5-0c298e46faa6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>request args for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205924177-b3b21172-6564-4585-9990-19383ce520a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>LIKE filter for name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205924450-cfc75c79-2389-4498-b839-fd3f7be0d73d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append sorting if column and order are provided and within the allows columsn<br>and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205925155-e1acb92a-28a8-4219-968a-f09b8c0d3dda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>end of the code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205931514-76364a6e-c173-4a96-8800-2274180da68b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company data table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205936045-93ee592a-a2ea-4092-b3dd-ad44bd3d02dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search engine with name.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205934428-4d1f05e2-7183-4c2e-81e6-92a8f321c068.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit file of company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205923804-88726f74-f2f5-4900-83a5-0c298e46faa6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name with the flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205924177-b3b21172-6564-4585-9990-19383ce520a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash messages with city<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205924450-cfc75c79-2389-4498-b839-fd3f7be0d73d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>continuation of the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205925155-e1acb92a-28a8-4219-968a-f09b8c0d3dda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>end of the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205863939-7b927c57-29a8-4616-8a6d-f169c6e61e24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205932644-a05b37b7-883a-4406-a2af-d3685959c3c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205907569-c0e39412-dfd7-4540-8d58-7e9b73fae1e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205936670-ecce25f8-282f-468f-bffa-ca1d4f4c2086.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205937559-154da407-28b2-45c3-8b80-a993a18816a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for the required file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205937724-5202c057-9631-412f-8c67-298524042c5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>end of the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205938028-e92e5cbe-4943-41b5-954b-7c37cba1b6aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code used to run the main file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205938239-d32fd675-cf6d-458f-8b83-0ad059a1f85e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>end of the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205939399-21f2f8d4-9c42-45ab-a110-def9c6f68465.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before the edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205939664-b5c42290-ea50-4a79-ab8d-6fb0e367189a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after the edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205938028-e92e5cbe-4943-41b5-954b-7c37cba1b6aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code to delete the file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205938239-d32fd675-cf6d-458f-8b83-0ad059a1f85e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>end of the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205863939-7b927c57-29a8-4616-8a6d-f169c6e61e24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before the edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205940960-7f514d4c-7895-4e2f-a0e0-9607b10688f1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after the edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113142876/205941383-a861815c-c6e3-41f3-b633-61b578b294eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>These are the test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>This project is a bit challenging than the previous projects. With this project<br>I have learnt the usage of .csv file and database output in the<br>website. The extra work on the html files made me to learn a<br>bit more about the language &quot;html&quot;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/sg2434" target="_blank">Grading</a></td></tr></table>