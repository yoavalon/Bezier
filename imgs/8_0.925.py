d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.long)

d.end()
