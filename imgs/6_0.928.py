d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SW, Length.long)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)

d.end()
