d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.NW, Orient.right, Length.long, Radius.high)
d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,3)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)

d.end()
