d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.SW, Length.long)
d.position_pen(0,2)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()
