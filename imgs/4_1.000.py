d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.NW, Length.short)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
