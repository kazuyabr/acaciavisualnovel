# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pesquisador")

image bg submarino = "images/bg submarino.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg submarino:
        zoom 2.1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    p "Você esta criando um novo Ren'Py game."

    p "Uma vez que você adicionou conteúdos aqui, sejam eles musicas, imagens de fundo, imagens de personagens, vc esta começando a criar seu roteiro!"

    # This ends the game.

    return
