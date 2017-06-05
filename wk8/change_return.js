/**
 * Created by michaelevan on 5/30/17.
 */

function transform(input) {
  if (input) {
    clearError();
    // do some transform of the user's input
    // vvvvvv HERE vvvvvv

    // your stuff HERE
    var cents = parseInt(input);

    var quarters = Math.floor(cents/25);
    var rem = cents - quarters * 25;

    var dimes = Math.floor(rem/10);
    rem = rem - dimes * 10;

    var nickels = Math.floor(rem/5);
    rem = rem - nickels * 5;

    var pennies = rem;

    var result = "Change is:" +
        quarters + "quarters"
        dimes + "dimes" +
        nickels + "nickels" +
        pennies + "pennies"

    print(result)

