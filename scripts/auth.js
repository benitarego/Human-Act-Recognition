document.addEventListener('DOMContentLoaded', function() {

    
    auth.onAuthStateChanged( user => {
        if (user) {
            console.log('user logged in: ', user);
        } else {
            console.log('user logged out');
        }
    })
    const signupform = document.querySelector('#signupform');
    if(signupform){
        signupform.addEventListener('submit', (e) => {
            e.preventDefault(); 
    
        //get user info
        const email = signupform['signup-email'].value;
        const password = signupform['signup-password'].value;
    
        //sign up the user
        auth.createUserWithEmailAndPassword(email, password)
        .then(
            user => {
            console.log('Account created for ' + user.email);
            db.collection('signup').add({
                iname: signupform.iname.value,
                dob: signupform.dob.value,
                address: signupform.address.value,
                uname: signupform.uname.value,
                relation: signupform.relation.value,
                contact: signupform.contact.value,
                email: signupform.email.value,
                password: signupform.password.value
             }) //.then(ref => {
            //     window.location.href = "dashboard.html";})
            .catch(error => {
                console.error("error adding", error);
            });
        }); 
        e.preventDefault();
    });
    }
    
//logout
const logout = document.querySelector('#logout');
if(logout){
    logout.addEventListener('click', (e) => {
        e.preventDefault();
    
        auth.signOut()
        .then(
            user => {
            console.log("user logged out");
        }) //.then(lref => {
            // window.location.href = "index.html";
        //})
        .catch(error => {
            console.error("error logging out", error);
        });
        e.preventDefault();
    });
}

//login
const signinform = document.querySelector('#signinform');
if(signinform){
    signinform.addEventListener('submit', (e) => {
        e.preventDefault();
    
        //get user info
        const email = signinform['signin-email'].value;
        const password = signinform['signin-password'].value;

        auth.signInWithEmailAndPassword(email, password)
        .then(
            user => {
                console.log('Signed in with ' + user.email);
            }) //.then(sref => {
              //  window.location.href = "dashboard.html";
            //})
            .catch(error => {
                console.error("error signing in", error);
            });
            e.preventDefault();
        });
    }
});
