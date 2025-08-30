// .pragma library

function sendMessage({
    // ОБЯЗАТЕЛЬНЫЕ ПАРПМЕТРЫ
    type = "text",         // Тип сообщения text/file/image/audio/video/location/reply и возможно в будущем другие
    senderId,              // Айди отправителя
    receiverId,            // Айди получателя
    
    // ОСНОВНЫЕ (НЕОБЯЗАТЕЛЬНЫЕ)
    text = "",             // Текст сообщения
    messageId = generateMessageId(),  // Уникальный айди
    
    // ДЛЯ РАЗНЫХ ТИПОВ
    fileData = null,       // Данные файла (для file/image/audio/video)
    location = null,       // Геолокацмя (для типа location если будем такой делать)
    replyTo = null,        // Ответ на сообщение (для reply типа)
    
    // МЕТАДАННЫЕ
    time = new Date().toISOString(),  // Время отправки
    signature = "",        // Подпись сообщения (на стороне отправителя в его сообщениии подписью будет его ник, а подписью чужого сообщения будет то имя, которое записано в контактах смотрящего пользователя либо тож ник)
    encryption = false,    // Зашифровано ли сообщение, по дефолту нет
}) {

    // БАЗОВЫЙ ОБЪЕКТ СООБЩЕНИЯ
    const baseMessage = {
        type: type,
        sender_id: senderId,
        receiver_id: receiverId,
        text: text,
        time: time,
        message_id: messageId,
        meta: {
            signature: signature,
            encryption: encryption,
        }
    };
    
    // ДОБАВЛЕНИЕ СПЕЦИФИЧЕСКИХ ДАННЫХ ПО ТИПУ
    switch (type) {
        case "file":
        case "image":
        case "audio":
        case "video":
            if (fileData) {
                baseMessage.file = {
                    src: fileData.src || "", // Путь к файлу
                    name: fileData.name || "", // Имя файла
                    size: fileData.size || 0, // Размер в байтах
                    mime_type: fileData.mimeType || "text/plain", // MIME тип
                    duration: fileData.duration || 0, // Длительность (аудио/видео)
                    thumbnail: fileData.thumbnail || "" // Превью (для изображений/видео)
                };
            }
            break;
            
        case "location":
            if (location) {
                baseMessage.location = {
                    latitude: location.lat,
                    longitude: location.lng,
                    accuracy: location.accuracy || 0,
                    address: location.address || "",
                    title: location.title || "Местоположение"
                };
            }
            break;
            
        case "reply":
            if (replyTo) {
                baseMessage.reply = {
                    message_id: replyTo.messageId,
                    sender_id: replyTo.senderId,
                    text: replyTo.text || "",
                    type: replyTo.type || "text"
                };
            }
            break;
    }
    
    // Проверка обязательныз полей
    if (!senderId || !receiverId) {
        throw new Error("senderId и receiverId обязательныее");
    }
    
    return JSON.stringify(baseMessage);
}

// Генератор рандом айди сообщениям
function generateMessageId() {
    return `msg_${Date.now()}_${Math.random().toString(36).substring(2, 9)}`;
}