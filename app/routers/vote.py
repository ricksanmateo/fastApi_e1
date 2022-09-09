from operator import mod
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import database, schemas, oauth2, models

router = APIRouter(
  prefix="/vote",
  tags=['Vote']
)


@router.post("/", status_code=status.HTTP_200_OK)
async def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
  
  post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id: {vote.post_id} does not exist')
  
  vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
  found_vote = vote_query.first()
  if (vote.dir == 1):
   if found_vote:
     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'user {current_user.id} has already voted {vote.post_id}')
   
   new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
   db.add(new_vote)
   db.commit()
   return {"Message": "Successfully added vote"}
  else:
    if not found_vote:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No vote found")
    
    vote_query.delete(synchronize_session=False)
    db.commit()
    
    return {"Message": "Successfully deleted vote"}