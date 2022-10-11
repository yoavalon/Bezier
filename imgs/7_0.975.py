d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.short)
d.position_pen(1,0)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NW, Length.medium)

d.end()
