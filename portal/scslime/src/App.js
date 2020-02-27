import React, {useState} from 'react';
import {DragDropContext, Droppable, Draggable} from 'react-beautiful-dnd'
import uuid from 'uuid/v4'

const book1 = [
    {id: uuid(), content: 'sam'},
    {id: uuid(), content: 'ron'},
    {id: uuid(), content: 'layla'},
    {id: uuid(), content: 'najiarry'}
];
const book2 = [
    {id: uuid(), content: 'ikeem'},
    {id: uuid(), content: 'kelsey'},
    {id: uuid(), content: 'mohamed'},
    {id: uuid(), content: 'apollo'},
    {id: uuid(), content: 'ethan'},
    {id: uuid(), content: 'kenny'}

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
};

function App() {
    const [columns, setColumns] = useState(clusterColumns);
    return (
        <div>
            <div style={{display: 'flex', justifyContent: 'left', height: '95%', position: "relative",
                top: 5, left: 90, opacity: '27%'}}>
                <DragDropContext onDragEnd={result => onDragEnd(result, columns, setColumns)}>
                    {Object.entries(columns).map(([id, column]) => {
                        return (
                            <div style={{display: 'flex', flexDirection: 'column', alignItems:'center',
                                fontFamily: 'Montez, sans-serif', color: '#913aff', fontSize: 27, padding:5, borderRadius: '19px',
                            }}><h2  style={{fontSize:(19*3), height: 45}}>{column.name}</h2>
                                <h2  style={{fontSize:(19*3), height: 45, top:'9px', position:'absolute', opacity:'60%', color:'#ffa0f9'}}>{column.name}</h2>
                                <div style={{margin: 2}}>
                                    <Droppable droppableId={id} key={id} >
                                        {(provided, snapshot) => {
                                            return (
                                                <div {...provided.droppableProps}
                                                     ref={provided.innerRef}
                                                     style={{
                                                         padding: 9,
                                                         width: 190,
                                                         minHeight: 9,
                                                         opacity: '95%',
                                                         borderRadius: '9px',
                                                         background: 'linear-gradient(to right bottom, rgba(196, 181, 255, 1), rgba(132,47,0,0.27)',

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
                                                                                    opacity: '95%',
                                                                                    userSelect: 'none',
                                                                                    padding: 19,
                                                                                    margin: '0px 0px 3px 0px',
                                                                                    backgroundColor: snapshot.isDragging ? '#54ffff':'#b3f542',
                                                                                    background: 'linear-gradient(to right bottom, rgba(84, 255, 255, 0.63), rgba(179, 245, 66, 0.81)',
                                                                                    color: 'rgb(115,38,0)' ,
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
