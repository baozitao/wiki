import os
import json
import win32com.client


def run(context):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True
    doc = word.Documents.Add()
    doc.Content.Text = "Hello from my Python Office Add-in!"
    doc.Save()

if __name__ == "__main__":
    run({})