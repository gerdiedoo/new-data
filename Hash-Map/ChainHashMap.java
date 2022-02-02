import java.util.ArrayList;
import java.util.Map.Entry;

/**
 * Classe nodo a ser utilizada para o ArrayList de buckets. Armazena um par key,
 * value. Tal como uma referência para o próximo nodo. Criando assim, uma lista
 * encadeada dentro de cada bucket.
 */
class Node {
    String key, value;
    Node next;

    public Node(String key, String value) {
        this.key = key;
        this.value = value;
    }
}

public class ChainHashMap extends AbstractMap {
    private ArrayList<Node> buckets;
    private int capacity;
    private int size;

    public ChainHashMap() {
        this.capacity = 10;
        initializeBuckets();
    }

    /**
     * Construtor parametrizado
     * 
     * @param capacity capacidade inicial dos buckets
     */
    public ChainHashMap(int capacity) {
        this.capacity = capacity;
        initializeBuckets();
    }

    /**
     * Inicializa uma lista de buckets de acordo com a capacidade
     */
    private void initializeBuckets() {
        buckets = new ArrayList<Node>(capacity);
        size = 0;
        for (int i = 0; i < capacity; i++) {
            buckets.add(null);
        }
    }

    /**
     * Calcula o fator de carga O fator de carga é calculado dividindo a quantidade
     * de elementos pela capacidade
     * 
     * @return o fator de carga
     */
    public Double getLoadFactor() {
        return (double) this.size / (double) this.capacity;
    }

    /**
     * Pega o primeiro item em uma lista encadeada de buckets
     * 
     * @param key key do item a ser procurado
     * @return o Nodo do primeiro item em determinado bucket
     */
    private Node getHead(String key) {
        int index = getIndex(key);
        return buckets.get(index);
    }

    /**
     * Pega o indice do bucket de determinada key. Transforma a key em hash e chama
     * o método de compressão
     * 
     * @param key key do item a ser procurado
     * @return o indice do bucket na ArrayList
     */
    private int getIndex(String key) {
        int hash = key.hashCode();
        int index = compress(hash);
        return index < 0 ? index * -1 : index;
    }

    /**
     * Realiza a compressão de determinado hash
     * 
     * @param hash o hash a ser comprimido
     * @return o índice do bucket pertencente ao hash
     */
    private int compress(long hash) {
        return (int) (hash % this.capacity);
    }

    /**
     * Dobra a capacidade de buckets
     */
    private void doubleCapacity() {
        ArrayList<Node> tempList = buckets;
        capacity *= 2;
        initializeBuckets();

        for (Node item : tempList) {
            while (item != null) {
                put(item.key, item.value);
                item = item.next;
            }
        }
    }

    /**
     * Retorna a quantidade de itens no map
     * 
     * @return quantidade de itens presentes
     */
    @Override
    public int size() {
        return this.size;
    }

    /**
     * Pega um item específico do map
     * 
     * @return o item de determinada key, ou null caso não encontre.
     */
    @Override
    public String get(String key) {
        Node head = getHead(key);
        while (head != null) {
            if (head.key.equals(key)) {
                return head.value;
            }
            head = head.next;
        }

        return null;
    }

    /**
     * Adiciona um par key-value. Esse método garante que não hajam colisões. Caso
     * dois hashs cheguem no mesmo índice após a compressão, o novo item é
     * adicionado na lista encadeada e a sua variável next aponta para o outro item
     * que estava como head da lista anteriormente. Após a inserção, se verifica o
     * fator de carga e se houver a necessidade, dobra a capacidade de buckets. Caso
     * a key ja exista, apenas adiciona o item da key.
     * 
     * @param key   chave do item a ser armazenado
     * @param value valor do itema ser armazenado
     * @return O valor antigo associado a chave, ou null se nenhum.
     */
    @Override
    public String put(String key, String value) {
        Node head = getHead(key);
        while (head != null) {
            if (head.key.equals(key)) {
                String lastValue = head.value;
                head.value = value;
                return lastValue;
            }
            head = head.next;
        }

        head = getHead(key);
        int indexInList = getIndex(key);
        Node newValue = new Node(key, value);
        newValue.next = head;
        buckets.set(indexInList, newValue);
        size++;

        if (getLoadFactor() >= 0.75) {
            doubleCapacity();
        }

        return null;
    }

    /**
     * Remove determinado chave-valor do bucket.
     * 
     * @param key chave do item a ser removido
     * @return valor associado a chave, ou null se não encontrar nenhum
     */
    @Override
    public String remove(String key) {
        int index = getIndex(key);
        Node head = getHead(key);
        Node prev = null;

        while (head != null) {
            if (head.key.equals(key)) {
                size--;
                if (prev != null) {
                    prev.next = head.next;
                } else {
                    buckets.set(index, head.next);
                }
                return head.value;
            }
            prev = head;
            head = head.next;
        }

        return null;
    }

    /**
     * Retorna o um valor iterável de todas as chaves armazenadas
     * 
     * @return Iterable com os valores das chaves
     */
    @Override
    public Iterable<String> keySet() {
        ArrayList<String> keys = new ArrayList<String>();
        for (Node item : buckets) {
            while (item != null) {
                keys.add(item.key);
                item = item.next;
            }
        }

        return keys;
    }

    /**
     * Retorna o um valor iterável de todos os valores armazenados
     * 
     * @return Iterable com todos os valores associados a alguma chave
     */
    @Override
    public Iterable<String> values() {
        ArrayList<String> keys = new ArrayList<String>();
        for (Node item : buckets) {
            while (item != null) {
                keys.add(item.value);
                item = item.next;
            }
        }

        return keys;
    }

    @Override
    public Iterable<Entry<String, String>> entrySet() {
        ArrayList<Entry<String, String>> keys = null;

        // for (Node item : buckets) {
        // Entry<String, String> entry = new Entry<String, String>(item.key,
        // item.value);
        // while (item != null) {
        // keys.add(item.key, item.value);
        // item = item.next;
        // }
        // }

        return keys;
    }

}
