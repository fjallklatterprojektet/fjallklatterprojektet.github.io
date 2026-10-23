
function expandTags()
{
  const expandTagsButton = document.getElementById("expand_tags_button");
  const expandableTags = document.getElementById("expandable_tags");

  if (expandTagsButton)
    expandTagsButton.style.display = 'none';
  
  if (expandableTags)
    expandableTags.style.display = 'inline';
}

function setupExpandableTags()
{
  const expandTagsButton = document.getElementById("expand_tags_button");
  const expandableTags = document.getElementById("expandable_tags");

  if (expandTagsButton)
    expandTagsButton.style.display = "inline-block";

  if (expandableTags)
    expandableTags.style.display = "none";
}
setupExpandableTags();
