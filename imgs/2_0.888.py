d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
