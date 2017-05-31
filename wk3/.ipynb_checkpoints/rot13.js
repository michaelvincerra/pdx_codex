
/**
 * Created by michaelevan on 5/30/17.
 */

/* """
Write a function to decrypt an ROT13 Enconded message.

"
"""

USE STRICT AT TOP

*/


var message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg.";


function rot13(message) {

    var encoded = message.toLowerCase();
    var alphabet = "abcdefghijklmnopqrstuvwxyz,-' ";
    var cesar13 = "nopqrstuvwxyzabcdefghijklm,-' ";

    var decoded = [];

    for (var i = 0;i< encoded.length; i++) {
        var enchar = encoded[i];
        var encloc = cesar13.indexOf(enchar);
        var decodedChar = alphabet[encloc];
        decoded.push(decodedChar);
    }

    var result = decoded.join('');
    document.write(result);

}

rot13(message);