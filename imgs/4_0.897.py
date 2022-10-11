d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,0)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)

d.end()
