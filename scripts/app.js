// const inputfield = document.querySelector('#input-field');
const form = document.querySelector("#signupform");

// create elements and render register
/*function renderRegister(doc) {
    let li = document.createElement('li');
    let iname = document.createElement('span');
    let dob = document.createElement('span');
    let address = document.createElement('span');
    let uname = document.createElement('span');
    let relation = document.createElement('span');  
    let contact = document.createElement('span');
    let email = document.createElement('span');
    let password = document.createElement('span');

    li.setAttribute('data-id', doc.id);
    // iname.textContent = doc.data().iname;
    // dob.textContent = doc.data().dob;
    // address.textContent = doc.data().address;
    // uname.textContent = doc.data().uname;
    // relation.textContent = doc.data().relation;
    // contact.textContent = doc.data().contact;
    // email.textContent = doc.data().email;
    // password.textContent = doc.data().password;

    // li.appendChild(iname);
    // li.appendChild(dob);
    // li.appendChild(address);
    // li.appendChild(uname);
    // li.appendChild(relation);
    // li.appendChild(contact);
    // li.appendChild(email);
    // li.appendChild(password);

    // inputfield.appendChild(li);
}*/

//getting data
/*db.collection('register').get().then((snapshot) => {
    snapshot.docs.forEach(doc => {
        renderRegister(doc);
    })
});*/

// saving data
form.addEventListener("submit", (e) => {
  e.preventDefault();
  db.collection("signup").add({
    iname: form.iname.value,
    dob: form.dob.value,
    address: form.address.value,
    uname: form.uname.value,
    relation: form.relation.value,
    contact: form.contact.value,
    email: form.email.value,
    password: form.password.value,
  });
});
db.collection("test")
  .doc("test")
  .set({
    test: "test",
  })
  .then(function () {
    console.log("success");
  });
