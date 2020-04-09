const signupform = document.querySelector('#signupform');
    signupform.addEventListener('submit', (e) => {
        e.preventDefault(); 
    //get user info
    const email = signupform['signup-email'].value;
    const password = signupform['signup-password'].value;

    console.log(email, password);
    //sign up the user
    /* auth.createUserWithEmailAndPassword(email, password).then(cred => {
        const modal = document.querySelector('#modal-signup');
        M.Modal.getInstance(modal).close();
        signupform.reset();
    }); */
});

//logout
/* const logout = document.querySelector('#logout');
logout.addEventListener('click', (e) => {
    e.preventDefault();
    auth.signOut().then(() => {
        console.log('user logged out');
    });
});
*/