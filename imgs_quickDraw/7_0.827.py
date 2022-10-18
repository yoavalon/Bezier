d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.NW, Length.long)

d.end()
