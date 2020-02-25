import React, {useState} from 'react';
import {DragDropContext, Draggable, Droppable} from 'react-beautiful-dnd'
// import {} from 'react-beautiful-dnd'
import uuid from 'uuid/v4'

const clusters = [
  {id: uuid(), content: 'tanna'},
  {id: uuid(), content: 'delhi'}
];

const clusterColumns = [
  {
    [uuid()]: {
      name: 'clusters',
      items: [clusters]
    }
  }
];


function App() {
  const [columns, setColumns]= useState(clusterColumns);

  return (
      <div>
    <div style={{display: 'flex', justifyContent: 'center', height: '19%', position: "absolute",
    top: 99, left: 450, opacity: '27%'}}>
      <DragDropContext onDropEnd={result => console.log(result)}>
        {Object.entries(columns).map((id, columns) => {
          return (
              <Droppable droppableId={id}>
                {(provided, snapshot) => {
                  return (
                      <div {...provided.droppableProps}
                        ref={provided.innerRef}
                        style={{
                          background: snapshot.isDraggingOver ? 'lightblue': 'lavender',
                          padding: 5,
                          width: 190,
                          minHeight: 450
                        }}>

                      </div>
                  )
                }}
              </Droppable>
          )
        })}
      </DragDropContext>
    </div>
        <div style={{display: 'flex', justifyContent: 'center', height: '19%', position: "absolute",
        top:90, left: 459, opacity: '9%'}}>
      <DragDropContext onDropEnd={result => console.log(result)}>
        {Object.entries(columns).map((id, columns) => {
          return (
              <Droppable droppableId={id}>
                {(provided, snapshot) => {
                  return (
                      <div {...provided.droppableProps}
                        ref={provided.innerRef}
                        style={{
                          background: snapshot.isDraggingOver ? 'lightblue': 'green',
                          padding: 5,
                          width: 190,
                          minHeight: 450
                        }}>

                      </div>
                  )
                }}
              </Droppable>
          )
        })}
      </DragDropContext>
    </div>
      </div>
  );
}

export default App;
