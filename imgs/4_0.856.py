d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)

d.end()
