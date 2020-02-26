import React, {useState} from 'react';
// import {DragDropContext, Draggable, Droppable} from 'react-beautiful-dnd'
import {DragDropContext, Droppable, Draggable} from 'react-beautiful-dnd'
import uuid from 'uuid/v4'

const book1 = [
        {id: uuid(), content: 'sam'},
        {id: uuid(), content: 'ron'},
        {id: uuid(), content: 'layla'},
    // {id: uuid(), content: 'north carolina'},
  // {id: uuid(), content: 'tanna'},
  // {id: uuid(), content: 'lubumbashi'},
  // {id: uuid(), content: 'papua new guinea'},
  // {id: uuid(), content: 'toronto'}
];
const book2 = [
    {id: uuid(), content: 'ikeem'},
    {id: uuid(), content: 'kelsey'},
    {id: uuid(), content: 'mohamed'},
    {id: uuid(), content: 'apollo'},
    {id: uuid(), content: 'ethan'},
    {id: uuid(), content: 'kenny'},

  // {id: uuid(), content: 'Whoever possesseth power over anything must elevate it to its uttermost perfection that it not be deprived of its own paradise. '},
  // {id: uuid(), content: 'Ye dwell in one world'},
  // {id: uuid(), content: 'Be ye as the fingers of one hand '},
  // {id: uuid(), content: 'Ye are all the leaves of one tree '},
  // {id: uuid(), content: 'The source of crafts, sciences and arts is the power of reflection'}

];
const book3 = [
    {id: uuid(), content: 'tayana'},
    {id: uuid(), content: 'miles'},
];

const clusterColumns =
    {
        [uuid()]: {
            name: 'Book 1',
            items: book1
        },
        [uuid()]: {
            name: 'Book 2',
            items: book2
        },
        [uuid()]: {
            name: 'Book 3',
            items: book3
        }
    };

const onDragEnd = (result, columns, setColumns ) => {
    if(!result.destination ) return;
    const {source, destination} = result;
    if (source.droppableId!==destination.droppableId) {
        const sourceColumn = columns[source.droppableId];
        const destColumn = columns[destination.droppableId];
        const sourceItems = [...sourceColumn.items];
        const destItems = [...destColumn.items];
        const [removed] = sourceItems.splice(source.index, 1);
        destItems.splice(destination.index, 0, removed);
        setColumns({
            ...columns,
            [source.droppableId]:{
                ...sourceColumn,
                items: sourceItems,
            },
            [destination.droppableId]:{
                ...destColumn,
                items: destItems
            }
        })
    }
    else {
        const column = columns[source.droppableId];
        const copiedItems = [...column.items];
        const [removed] = copiedItems.splice(source.index, 1);
        copiedItems.splice(destination.index, 0, removed)
        setColumns({
            ...columns,
            [source.droppableId]: {
                ...column,
                items: copiedItems
            }
        })
    }

}

function App() {
  const [columns, setColumns] = useState(clusterColumns);
  return (
      <div>
        <div style={{display: 'flex', justifyContent: 'left', height: '95%', position: "relative",
          top: 19, left: 90, opacity: '27%'}}>
          <DragDropContext onDragEnd={result => onDragEnd(result, columns, setColumns)}>
            {Object.entries(columns).map(([id, column]) => {
              return (
                  <div style={{display: 'flex', flexDirection: 'column', alignItems:'center', 
                  fontFamily: 'Montez, sans-serif', color: '#913aff', fontSize: 27, padding:0}}><h2  style={{fontSize:(19*3), height: 45}}>{column.name}</h2>
                    <div style={{margin: 2}}>
                      <Droppable droppableId={id} key={id} >
                    {(provided, snapshot) => {
                      return (
                          <div {...provided.droppableProps}
                               ref={provided.innerRef}
                               style={{
                                 background: 'rgba(145,58,255,0.45)',
                                 padding: 9,
                                 width: 270,
                                 minHeight: 19,
                                 opacity: '90%',
                                 borderRadius: '7px'
                               }}
                          >
                            {column.items.map((item, index) => {
                                  return (
                                      <Draggable key={item.id} draggableId={item.id} index={index}>
                                        {(provided, snapshot) => {
                                          return (
                                              <div
                                                  ref={provided.innerRef}
                                                  {...provided.draggableProps}
                                                  {...provided.dragHandleProps}
                                                  style={{
                                                    opacity: '90%',
                                                    userSelect: 'none',
                                                    padding: 19,
                                                    margin: '0 0 9px 0',
                                                    backgroundColor: snapshot.isDragging ? '#54ffff':'#b3f542',
                                                    color: 'rgba(132,47,0,0.96)' ,
                                                    fontFamily: 'Montez',
                                                    fontSize: 36,
                                                    borderRadius: '9px',

                                                    ...provided.draggableProps.style
                                                  }}
                                              >
                                                {item.content}
                                              </div>

                                          )
                                        }}
                                      </Draggable>
                                  )
                                }
                            )}
                              {provided.placeholder}
                          </div>
                      )
                    }}
                  </Droppable>
                  </div>
                      </div>
              )
            })}
          </DragDropContext>
        </div>
      </div>
  );
}

export default App;
