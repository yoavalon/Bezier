d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,2)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)

d.end()
