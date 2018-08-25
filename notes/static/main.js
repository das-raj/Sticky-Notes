bkLib.onDomLoaded(nicEditors.allTextAreas);
/*bkLib.onDomLoaded(function() { new nicEditor({fullPanel : true}).panelInstance('new_note_text-area') });*/

function editVisible(id)
{
    visible = document.getElementById("edit_btn"+id).style.display;
    if(visible == "none")
    {
        document.getElementById("edit_btn"+id).style.display="block";
        document.getElementById("text_area"+id).disabled=false;
        
    }
    else{
        document.getElementById("edit_btn"+id).style.display="none";
        document.getElementById("text_area"+id).disabled=true;    }
}