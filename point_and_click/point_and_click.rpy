########## DEVIL SPIδεR'S POINT'n'CLICK PLUGIN ##########
# This plugin implements a modular point'n'click feature to make gameplay more interactive
# Currently supported features:
#   - Conditional interaction - make interactions available only when a certain condition is met
#   - Perspective switching - make segments take place in multiple rooms or angles
#   - Multiple ways to start or end one point'n'click segment - it's all a matter of jumping in and out of the segment

## Parameters ##
# There are numerous occasions where I list out a format for parameters. If the argument is in quotation marks in the format (like "this")
# the argument should also be in quotation marks

## Images ##
# There should an arbitrary amount of image pairs in game/point_and_click/image:
# the pair should consist of images in the filename format of X_idle.png and X_hover.png, where X is a word or a phrase
# this will be needed later in the plugin.

# This is the code that renders the point'n'click elements to the player

# To see steps necessary outside the PnC segments that initialize them, see the demo game's script.rpy file
# If you don't have the demo script, the rundown is that you have to set the current_room variable correctly and start the segment like this:
#   $ current_room = "example" # this value can be changed
#   jump pnc_loop

init -3:
    default pnc_flags = {} # This variable controls various creator-defined flags that control the state of a given point'n'click segment

screen pnc_screen(room_name):

    style_prefix "pnc"

    for i in buttons:
        if (i[3] is None) or (eval(i[3])):
            imagebutton auto "point_and_click/image/" + str(i[0]) + "_%s.png" pos i[1] action Return(i[2])

style pnc_image_button:
    anchor (0.5, 0.5)

define diss = {"screens" : Dissolve(0.15)} # this allows the textbox to be hidden and shown without any pause

# This label handles showing the screen to the player.
label pnc_loop:
    $ quick_menu = False
    window hide diss
    call screen pnc_screen(current_room)
    window show diss
    $ quick_menu = True
    jump expression _return

### INTERACTION LISTS ###
# The plugin supports creation of an unlimited amount of so-called interaction lists, which are Python lists of tuples of a given format:
# (("image_name"),(x_coordinate, y_coordinate),"label_name", condition),
# - image_name represents a string that will determine the button's appearance. To demonstrate with an example, if this parameter was "dog",
# then the plug-in expects dog_idle.png and dog_hover.png to exist in game/point_and_click/image.
# - x_coordinate and y_coordinate correspond to the position of the button in the screen, relative to the button's center.
# - label_name represents the label that triggers when that button is pressed.
# - conditions corresponds to either:
# -- a string containing Python expression that determines the button's visibility - it shows when the condition is True
# -- the None value - making the button visible at all times
# The lists should end in _buttons

define buttons = [
    (("Lihat"),(1659, 300),"Cromboloni", "not (pnc_flags.get('Cromboloni', False) or pnc_flags.get('Kue_Tomas', False) or pnc_flags.get('Cream_Tart', False))"),
    (("Lihat"),(1181, 301),"Kue_Tomas", "not (pnc_flags.get('Cromboloni', False) or pnc_flags.get('Kue_Tomas', False) or pnc_flags.get('Cream_Tart', False))"),
    (("Lihat"),(1667, 791),"Cream_Tart", "not (pnc_flags.get('Cromboloni', False) or pnc_flags.get('Kue_Tomas', False) or pnc_flags.get('Cream_Tart', False))"),
    (("Bayar"),(485, 759),"Bayar", "pnc_flags.get('Cromboloni', False) or pnc_flags.get('Kue_Tomas', False) or pnc_flags.get('Cream_Tart', False)"), 
]

### POINT'n'CLICK LABELS ###
# Labels within a point'n'click segment almost always end in a jump statement.


label Cromboloni:
    "Cromboloni, adonan kroisan berbentuk lingkaran, diisi dengan krim pastri, bagian atas diberi aneka toping."
    "Tersisa rasa coklat saja."
    "Tak terlihat terlalu spesial."
    menu:
     "Aku beli ga ya?"

     "Beli":
         $ pnc_flags["Cromboloni"] = True # this adds a key-value pair into the pnc_flags dictionary.
         "Pasti Angel suka! {p}Bayar ah~"
         jump pnc_loop
     "Ga ah, mau milih yang lain":
        jump pnc_loop

label Kue_Tomas:
    "Kue Tomas The Engine, Kue fondan simple dengan mainan Tomas The Engine diatasnya."
    "Lilinnya jatuh satu."
    "Seperti untuk anak kecil."
    menu:
     "Aku beli ga ya?"

     "Beli":
         $ pnc_flags["Kue_Tomas"] = True # this adds a key-value pair into the pnc_flags dictionary.
         "Pasti Angel suka! {p}Bayar ah~"
         jump pnc_loop
     "Ga ah, mau milih yang lain":
         jump pnc_loop

label Cream_Tart:
    "Cream tart. Terbuat dari adonan ditumpuk diatas satu sama lain."
    "Tulisannya '67' dan krimnya sedikit kemana-mana."
    "Tak terlihat terlalu serius."
    menu:
     "Aku beli ga ya?"

     "Beli":
         $ pnc_flags["Cream_Tart"] = True # this adds a key-value pair into the pnc_flags dictionary.
         "Pasti Angel suka! {p}Bayar ah~"
         jump pnc_loop
     "Ga ah, mau milih yang lain":
         jump pnc_loop

label Bayar:
    "Sudah ada kasir yang menyapamu dengan senyum manis. “Mau beli, kak? Disini QRIS-only ya. {i}By the way{/i}, maaf ya ka, banyak yang stoknya habis.”"
    "Aku mengangguk malu-malu dan menscan QRIS."
    
    if pnc_flags.get("Cromboloni") == True:
        "Aku mengambil Cromboloni rasa coklat."
    elif pnc_flags.get("Kue_Tomas") == True:
        "Aku mengambil Kue Tomas The Engine."
    elif pnc_flags.get("Cream_Tart") == True:
        "Aku mengambil Cream Tart bertuliskan '67'."

    "Aku berjalan keluar toko."
    jump end