import Crime_Printer as Crime_Printer
from Models import Game

game = Game()
Crime_Printer.save_crimes(game.crimes)