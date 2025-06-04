CREATE TABLE entity (
    id SERIAL PRIMARY KEY, -- 'SERIAL' auto-increments and creates a unique primary key
    title VARCHAR(255) NOT NULL -- Stores the entity's title, cannot be empty
);

-- Table: product
-- Stores product information, including a reference to its associated entity.
CREATE TABLE product (
    id SERIAL PRIMARY KEY, -- 'SERIAL' auto-increments and creates a unique primary key
    title VARCHAR(255) NOT NULL, -- Stores the product's title, cannot be empty
    no INTEGER NOT NULL
);

-- Table: model_version
-- Stores information about different versions of your trained YOLOv8 models.
-- Each model version has a unique ID, a path to its stored file (e.g., .pt file),
-- and a descriptive title.
CREATE TABLE model_version (
    id SERIAL PRIMARY KEY,      -- Auto-incrementing unique ID for each model version
    path VARCHAR(512) NOT NULL, -- The file path where the model (.pt file) is stored
                                -- (e.g., 'runs/detect/my_yolov8_custom_training/weights/best.pt')
    title VARCHAR(255) NOT NULL UNIQUE -- A descriptive title for the model version (e.g., 'YOLOv8 Prod v1.0'),
                                       -- enforced as unique for easy identification
);

-- Table: entity_model_version
-- This is a join table that creates a many-to-many relationship between
-- 'entity' and 'model_version'. This means one entity can be associated
-- with multiple model versions, and one model version can be associated
-- with multiple entities.
CREATE TABLE entity_model_version (
    id SERIAL PRIMARY KEY,      -- Unique ID for each association entry (optional, but good practice)
    entity_id INTEGER NOT NULL, -- Foreign key referencing the 'entity' table
    model_version_id INTEGER NOT NULL, -- Foreign key referencing the 'model_version' table

    -- Define foreign key constraints
    CONSTRAINT fk_entity_id_emv
        FOREIGN KEY (entity_id)
        REFERENCES entity (id), -- If an entity is deleted, its associations here are also deleted

    CONSTRAINT fk_model_version_id_emv
        FOREIGN KEY (model_version_id)
        REFERENCES model_version (id), -- If a model version is deleted, its associations here are also deleted

    -- Ensure that each entity-model_version pair is unique
    -- This prevents duplicate associations
    CONSTRAINT unique_entity_model_version
        UNIQUE (entity_id, model_version_id)
);