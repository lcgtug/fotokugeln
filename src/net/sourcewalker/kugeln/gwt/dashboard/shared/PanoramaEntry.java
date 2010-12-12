package net.sourcewalker.kugeln.gwt.dashboard.shared;

import java.io.Serializable;

public class PanoramaEntry implements Serializable {

    private static final long serialVersionUID = -331537782469475035L;

    private String key;
    private String name;
    private String status;
    private boolean thumbnail;

    public String getKey() {
        return key;
    }

    public String getName() {
        return name;
    }

    public String getStatus() {
        return status;
    }

    public boolean hasThumbnail() {
        return thumbnail;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public void setThumbnail(boolean thumbnail) {
        this.thumbnail = thumbnail;
    }

}