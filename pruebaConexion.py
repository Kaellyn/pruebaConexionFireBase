import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def conectar():
    print("\n**** Conectando Base *****")
    cred = credentials.Certificate("pruebasproyectos-d9fe8-firebase-adminsdk-xi2n1-39af5e33f4.json")
    firebase_admin.initialize_app(cred, {
        'projectId': 'pruebasproyectos-d9fe8',
    })
    db = firestore.client()
    return db
    
def insertar(db):
    print("\n**** Insertando *****")
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })

    doc_ref = db.collection(u'users').document(u'aturing')
    doc_ref.set({
        u'first': u'Alan',
        u'middle': u'Mathison',
        u'last': u'Turing',
        u'born': 1912
    })

def imprimir(db):
    print("\n**** Imprimiendo *****")
    users_ref = db.collection(u'users')
    docs = users_ref.stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

def borrar(db):
    print("\n**** Borrando *****")
    db.collection(u'users').document(u'alovelace').delete()


def actualizar(db):
    print("\n**** Actualizando *****")
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.update({
        u'born': 1830
    })

if __name__ == "__main__":
    db = conectar()
    insertar(db)
    imprimir(db)
    actualizar(db)
    imprimir(db)
    borrar(db)
    imprimir(db)